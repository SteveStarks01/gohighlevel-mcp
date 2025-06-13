import React from 'react';
import { Bot, User, Info } from 'lucide-react';
import { formatDistanceToNow } from 'date-fns';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

interface Message {
  id: string;
  type: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: string;
  intent?: string;
  data?: any;
}

interface ChatMessageProps {
  message: Message;
}

const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
  const isUser = message.type === 'user';
  const isSystem = message.type === 'system';

  if (isSystem) {
    return (
      <div className="flex justify-center">
        <div className="flex items-center space-x-2 bg-blue-50 text-blue-700 px-4 py-2 rounded-full text-sm">
          <Info className="w-4 h-4" />
          <span>{message.content}</span>
        </div>
      </div>
    );
  }

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} animate-slide-up`}>
      <div className={`flex max-w-3xl ${isUser ? 'flex-row-reverse' : 'flex-row'} space-x-3`}>
        {/* Avatar */}
        <div className={`flex-shrink-0 ${isUser ? 'ml-3' : 'mr-3'}`}>
          <div className={`w-8 h-8 rounded-full flex items-center justify-center ${
            isUser 
              ? 'bg-primary-600 text-white' 
              : 'bg-gray-100 text-gray-600'
          }`}>
            {isUser ? <User className="w-4 h-4" /> : <Bot className="w-4 h-4" />}
          </div>
        </div>

        {/* Message content */}
        <div className={`flex-1 ${isUser ? 'text-right' : 'text-left'}`}>
          <div className={`inline-block px-4 py-3 rounded-2xl ${
            isUser
              ? 'bg-primary-600 text-white'
              : 'bg-white border border-gray-200 text-gray-900'
          }`}>
            <div className="prose prose-sm max-w-none">
              <ReactMarkdown 
                remarkPlugins={[remarkGfm]}
                className={`${isUser ? 'text-white' : 'text-gray-900'}`}
                components={{
                  // Customize markdown components for better styling
                  p: ({ children }) => <p className="mb-2 last:mb-0">{children}</p>,
                  ul: ({ children }) => <ul className="list-disc list-inside mb-2">{children}</ul>,
                  ol: ({ children }) => <ol className="list-decimal list-inside mb-2">{children}</ol>,
                  li: ({ children }) => <li className="mb-1">{children}</li>,
                  code: ({ children }) => (
                    <code className={`px-1 py-0.5 rounded text-xs ${
                      isUser 
                        ? 'bg-primary-700 text-primary-100' 
                        : 'bg-gray-100 text-gray-800'
                    }`}>
                      {children}
                    </code>
                  ),
                  pre: ({ children }) => (
                    <pre className={`p-3 rounded-lg text-xs overflow-x-auto ${
                      isUser 
                        ? 'bg-primary-700 text-primary-100' 
                        : 'bg-gray-100 text-gray-800'
                    }`}>
                      {children}
                    </pre>
                  ),
                }}
              >
                {message.content}
              </ReactMarkdown>
            </div>
          </div>

          {/* Data visualization for assistant messages */}
          {!isUser && message.data && message.data.success && (
            <div className="mt-3">
              <DataVisualization data={message.data} intent={message.intent} />
            </div>
          )}

          {/* Timestamp */}
          <div className={`text-xs text-gray-500 mt-1 ${isUser ? 'text-right' : 'text-left'}`}>
            {formatDistanceToNow(new Date(message.timestamp), { addSuffix: true })}
            {message.intent && (
              <span className="ml-2 px-2 py-0.5 bg-gray-100 text-gray-600 rounded-full">
                {message.intent}
              </span>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

// Component to visualize data from MCP tool responses
const DataVisualization: React.FC<{ data: any; intent?: string }> = ({ data, intent }) => {
  if (!data.data) return null;

  const renderContactsList = (contacts: any[]) => (
    <div className="bg-gray-50 rounded-lg p-4 mt-2">
      <h4 className="font-medium text-gray-900 mb-3">Contacts ({contacts.length})</h4>
      <div className="space-y-2">
        {contacts.slice(0, 5).map((contact, index) => (
          <div key={index} className="flex items-center justify-between bg-white p-3 rounded-lg">
            <div>
              <p className="font-medium text-gray-900">{contact.name}</p>
              <p className="text-sm text-gray-500">{contact.email}</p>
            </div>
            {contact.phone && (
              <p className="text-sm text-gray-600">{contact.phone}</p>
            )}
          </div>
        ))}
        {contacts.length > 5 && (
          <p className="text-sm text-gray-500 text-center py-2">
            ... and {contacts.length - 5} more
          </p>
        )}
      </div>
    </div>
  );

  const renderOpportunitiesList = (opportunities: any[]) => (
    <div className="bg-gray-50 rounded-lg p-4 mt-2">
      <h4 className="font-medium text-gray-900 mb-3">Opportunities ({opportunities.length})</h4>
      <div className="space-y-2">
        {opportunities.slice(0, 5).map((opp, index) => (
          <div key={index} className="flex items-center justify-between bg-white p-3 rounded-lg">
            <div>
              <p className="font-medium text-gray-900">{opp.name}</p>
              <p className="text-sm text-gray-500">{opp.stage}</p>
            </div>
            <div className="text-right">
              <p className="font-medium text-green-600">
                ${opp.value?.toLocaleString() || '0'}
              </p>
            </div>
          </div>
        ))}
        {opportunities.length > 5 && (
          <p className="text-sm text-gray-500 text-center py-2">
            ... and {opportunities.length - 5} more
          </p>
        )}
      </div>
    </div>
  );

  const renderAppointmentsList = (appointments: any[]) => (
    <div className="bg-gray-50 rounded-lg p-4 mt-2">
      <h4 className="font-medium text-gray-900 mb-3">Appointments ({appointments.length})</h4>
      <div className="space-y-2">
        {appointments.slice(0, 5).map((apt, index) => (
          <div key={index} className="flex items-center justify-between bg-white p-3 rounded-lg">
            <div>
              <p className="font-medium text-gray-900">{apt.title}</p>
              <p className="text-sm text-gray-500">{apt.contact}</p>
            </div>
            <div className="text-right">
              <p className="text-sm text-gray-600">{apt.time}</p>
              {apt.duration && (
                <p className="text-xs text-gray-500">{apt.duration}</p>
              )}
            </div>
          </div>
        ))}
        {appointments.length > 5 && (
          <p className="text-sm text-gray-500 text-center py-2">
            ... and {appointments.length - 5} more
          </p>
        )}
      </div>
    </div>
  );

  const renderKPIs = (kpis: any) => (
    <div className="bg-gray-50 rounded-lg p-4 mt-2">
      <h4 className="font-medium text-gray-900 mb-3">Key Metrics</h4>
      <div className="grid grid-cols-2 gap-4">
        {Object.entries(kpis).map(([key, value]) => (
          <div key={key} className="bg-white p-3 rounded-lg text-center">
            <p className="text-2xl font-bold text-gray-900">
              {typeof value === 'number' && key.includes('value') 
                ? `$${value.toLocaleString()}` 
                : String(value)}
            </p>
            <p className="text-sm text-gray-500 capitalize">
              {key.replace(/_/g, ' ')}
            </p>
          </div>
        ))}
      </div>
    </div>
  );

  // Render based on intent and data structure
  if (intent === 'show_contacts' && data.data.contacts) {
    return renderContactsList(data.data.contacts);
  }

  if (intent === 'show_opportunities' && data.data.opportunities) {
    return renderOpportunitiesList(data.data.opportunities);
  }

  if (intent === 'show_appointments' && data.data.appointments) {
    return renderAppointmentsList(data.data.appointments);
  }

  if (intent === 'show_analytics' && data.data.kpis) {
    return renderKPIs(data.data.kpis);
  }

  // Generic data display
  return (
    <div className="bg-gray-50 rounded-lg p-4 mt-2">
      <pre className="text-xs text-gray-600 overflow-x-auto">
        {JSON.stringify(data.data, null, 2)}
      </pre>
    </div>
  );
};

export default ChatMessage;
