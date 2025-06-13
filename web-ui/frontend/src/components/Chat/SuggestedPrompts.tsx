import React from 'react';
import { 
  Calendar, 
  Users, 
  Target, 
  MessageSquare, 
  BarChart3,
  UserPlus,
  TrendingUp,
  Clock
} from 'lucide-react';

interface SuggestedPromptsProps {
  onPromptClick: (prompt: string) => void;
}

const SuggestedPrompts: React.FC<SuggestedPromptsProps> = ({ onPromptClick }) => {
  const prompts = [
    {
      text: "Show me today's appointments",
      icon: Calendar,
      category: "Calendar",
      color: "bg-blue-50 text-blue-700 hover:bg-blue-100"
    },
    {
      text: "What's my pipeline looking like?",
      icon: Target,
      category: "Sales",
      color: "bg-green-50 text-green-700 hover:bg-green-100"
    },
    {
      text: "Create a new contact for John Doe",
      icon: UserPlus,
      category: "Contacts",
      color: "bg-purple-50 text-purple-700 hover:bg-purple-100"
    },
    {
      text: "Show recent conversations",
      icon: MessageSquare,
      category: "Messages",
      color: "bg-orange-50 text-orange-700 hover:bg-orange-100"
    },
    {
      text: "Show me this week's performance",
      icon: BarChart3,
      category: "Analytics",
      color: "bg-indigo-50 text-indigo-700 hover:bg-indigo-100"
    },
    {
      text: "List contacts created this month",
      icon: Users,
      category: "Contacts",
      color: "bg-pink-50 text-pink-700 hover:bg-pink-100"
    },
    {
      text: "What opportunities need follow-up?",
      icon: TrendingUp,
      category: "Sales",
      color: "bg-cyan-50 text-cyan-700 hover:bg-cyan-100"
    },
    {
      text: "Schedule a demo for tomorrow",
      icon: Clock,
      category: "Calendar",
      color: "bg-yellow-50 text-yellow-700 hover:bg-yellow-100"
    }
  ];

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 max-w-2xl mx-auto">
      {prompts.map((prompt, index) => {
        const Icon = prompt.icon;
        
        return (
          <button
            key={index}
            onClick={() => onPromptClick(prompt.text)}
            className={`flex items-center space-x-3 p-4 rounded-xl border border-gray-200 transition-all duration-200 hover:shadow-md hover:scale-105 ${prompt.color}`}
          >
            <div className="flex-shrink-0">
              <Icon className="w-5 h-5" />
            </div>
            <div className="flex-1 text-left">
              <p className="text-sm font-medium">
                {prompt.text}
              </p>
              <p className="text-xs opacity-75 mt-1">
                {prompt.category}
              </p>
            </div>
          </button>
        );
      })}
    </div>
  );
};

export default SuggestedPrompts;
