import React, { useState, useRef, useEffect } from 'react';
import { Bot, Loader2 } from 'lucide-react';
import { useWebSocket } from '../../hooks/useWebSocket';
import ChatMessage from './ChatMessage';
import TypingIndicator from './TypingIndicator';
import SuggestedPrompts from './SuggestedPrompts';
import { PromptInputBox } from '../ui/ai-prompt-box';

interface Message {
  id: string;
  type: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: string;
  intent?: string;
  data?: any;
}

const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isTyping, setIsTyping] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // WebSocket connection
  const { sendMessage, isConnected } = useWebSocket({
    url: 'ws://localhost:8000/ws/chat',
    onMessage: (data) => {
      if (data.type === 'message') {
        const newMessage: Message = {
          id: `msg_${Date.now()}`,
          type: 'assistant',
          content: data.message,
          timestamp: data.timestamp,
          intent: data.intent,
          data: data.data,
        };
        setMessages(prev => [...prev, newMessage]);
        setIsTyping(false);
      } else if (data.type === 'typing') {
        setIsTyping(data.is_typing);
      } else if (data.type === 'system') {
        const systemMessage: Message = {
          id: `sys_${Date.now()}`,
          type: 'system',
          content: data.message,
          timestamp: data.timestamp,
        };
        setMessages(prev => [...prev, systemMessage]);
      }
    },
  });

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  const handleSendMessage = (message: string) => {
    if (!message.trim() || !isConnected) return;

    // Add user message to chat
    const userMessage: Message = {
      id: `msg_${Date.now()}`,
      type: 'user',
      content: message,
      timestamp: new Date().toISOString(),
    };

    setMessages(prev => [...prev, userMessage]);

    // Send message via WebSocket
    sendMessage({
      type: 'chat',
      message: message,
      conversation_id: 'default',
    });

    // Show typing indicator
    setIsTyping(true);
    setIsLoading(true);
  };

  const handleSuggestedPrompt = (prompt: string) => {
    handleSendMessage(prompt);
  };

  // Update loading state when typing indicator changes
  useEffect(() => {
    if (!isTyping) {
      setIsLoading(false);
    }
  }, [isTyping]);

  return (
    <div className="flex flex-col h-96">
      {/* Connection status */}
      {!isConnected && (
        <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4 mb-4">
          <div className="flex">
            <div className="flex-shrink-0">
              <Loader2 className="h-5 w-5 text-yellow-400 animate-spin" />
            </div>
            <div className="ml-3">
              <p className="text-sm text-yellow-700">
                Connecting to AI Assistant...
              </p>
            </div>
          </div>
        </div>
      )}

      {/* Messages area */}
      <div className="flex-1 overflow-y-auto chat-scrollbar px-4 py-2 space-y-4">
        {messages.length === 0 && (
          <div className="text-center py-8">
            <div className="inline-flex items-center justify-center w-16 h-16 bg-primary-100 rounded-full mb-4">
              <Bot className="w-8 h-8 text-primary-600" />
            </div>
            <h3 className="text-lg font-medium text-gray-900 mb-2">
              Welcome to your AI Assistant
            </h3>
            <p className="text-gray-500 mb-6 max-w-md mx-auto">
              I can help you manage your GoHighLevel data, create contacts, schedule appointments, 
              analyze your pipeline, and much more. What would you like to do?
            </p>
            <SuggestedPrompts onPromptClick={handleSuggestedPrompt} />
          </div>
        )}

        {messages.map((message) => (
          <ChatMessage key={message.id} message={message} />
        ))}

        {isTyping && <TypingIndicator />}
        
        <div ref={messagesEndRef} />
      </div>

      {/* AI Prompt Box Input */}
      <div className="border-t border-gray-200 p-4">
        <PromptInputBox
          onSend={handleSendMessage}
          placeholder="Ask me anything about your GoHighLevel data..."
          isLoading={isLoading}
          className="w-full"
        />

        {/* Quick actions */}
        {messages.length > 0 && (
          <div className="mt-3 flex flex-wrap gap-2">
            <button
              onClick={() => handleSuggestedPrompt("Show me today's appointments")}
              className="text-xs px-3 py-1 bg-gray-100 text-gray-700 rounded-full hover:bg-gray-200 transition-colors disabled:opacity-50"
              disabled={isLoading}
            >
              Today's appointments
            </button>
            <button
              onClick={() => handleSuggestedPrompt("What's my pipeline looking like?")}
              className="text-xs px-3 py-1 bg-gray-100 text-gray-700 rounded-full hover:bg-gray-200 transition-colors disabled:opacity-50"
              disabled={isLoading}
            >
              Pipeline status
            </button>
            <button
              onClick={() => handleSuggestedPrompt("Show recent contacts")}
              className="text-xs px-3 py-1 bg-gray-100 text-gray-700 rounded-full hover:bg-gray-200 transition-colors disabled:opacity-50"
              disabled={isLoading}
            >
              Recent contacts
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default ChatInterface;
