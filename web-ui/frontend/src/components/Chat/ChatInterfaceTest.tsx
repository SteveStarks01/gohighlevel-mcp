import React, { useState } from 'react';
import { PromptInputBox } from '../ui/ai-prompt-box';

/**
 * Test component to verify the AI Prompt Box integration
 * This can be used for testing the component in isolation
 */
const ChatInterfaceTest: React.FC = () => {
  const [messages, setMessages] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSendMessage = (message: string) => {
    console.log('Message sent:', message);
    
    // Add message to list
    setMessages(prev => [...prev, message]);
    
    // Simulate loading
    setIsLoading(true);
    
    // Simulate AI response after 2 seconds
    setTimeout(() => {
      setMessages(prev => [...prev, `AI Response to: "${message}"`]);
      setIsLoading(false);
    }, 2000);
  };

  return (
    <div className="max-w-2xl mx-auto p-6 space-y-4">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">
        AI Prompt Box Integration Test
      </h1>
      
      {/* Messages Display */}
      <div className="space-y-2 mb-6">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`p-3 rounded-lg ${
              index % 2 === 0
                ? 'bg-blue-50 text-blue-900 ml-0 mr-8'
                : 'bg-gray-50 text-gray-900 ml-8 mr-0'
            }`}
          >
            {message}
          </div>
        ))}
        
        {isLoading && (
          <div className="bg-gray-50 text-gray-900 ml-8 mr-0 p-3 rounded-lg">
            <div className="flex items-center space-x-2">
              <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-gray-900"></div>
              <span>AI is thinking...</span>
            </div>
          </div>
        )}
      </div>

      {/* AI Prompt Box */}
      <div className="border-t border-gray-200 pt-4">
        <PromptInputBox
          onSend={handleSendMessage}
          placeholder="Test the AI Prompt Box here..."
          isLoading={isLoading}
          className="w-full"
        />
      </div>

      {/* Test Instructions */}
      <div className="mt-8 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
        <h3 className="font-semibold text-yellow-800 mb-2">Test Features:</h3>
        <ul className="text-sm text-yellow-700 space-y-1">
          <li>• Type a message and press Enter or click send</li>
          <li>• Test auto-expanding textarea</li>
          <li>• Verify loading states and animations</li>
          <li>• Test keyboard shortcuts (Enter to send, Shift+Enter for new line)</li>
          <li>• Verify disabled state when loading</li>
          <li>• Test empty message handling</li>
        </ul>
      </div>
    </div>
  );
};

export default ChatInterfaceTest;
