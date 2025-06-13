import React from 'react';
import { Bot } from 'lucide-react';

const TypingIndicator: React.FC = () => {
  return (
    <div className="flex justify-start animate-slide-up">
      <div className="flex max-w-3xl flex-row space-x-3">
        {/* Avatar */}
        <div className="flex-shrink-0 mr-3">
          <div className="w-8 h-8 rounded-full flex items-center justify-center bg-gray-100 text-gray-600">
            <Bot className="w-4 h-4" />
          </div>
        </div>

        {/* Typing indicator */}
        <div className="flex-1">
          <div className="inline-block px-4 py-3 rounded-2xl bg-white border border-gray-200">
            <div className="typing-indicator">
              <div className="typing-dot"></div>
              <div className="typing-dot"></div>
              <div className="typing-dot"></div>
            </div>
          </div>
          <div className="text-xs text-gray-500 mt-1">
            AI is thinking...
          </div>
        </div>
      </div>
    </div>
  );
};

export default TypingIndicator;
