import React from 'react';
import { NavLink } from 'react-router-dom';
import {
  LayoutDashboard,
  Users,
  MessageSquare,
  Target,
  Calendar,
  FileText,
  Building2,
  Settings,
  BarChart3,
  Bot
} from 'lucide-react';

const navigation = [
  { name: 'Dashboard', href: '/dashboard', icon: LayoutDashboard },
  { name: 'AI Assistant', href: '/chat', icon: Bot },
  { name: 'Contacts', href: '/contacts', icon: Users },
  { name: 'Conversations', href: '/conversations', icon: MessageSquare },
  { name: 'Opportunities', href: '/opportunities', icon: Target },
  { name: 'Calendar', href: '/calendar', icon: Calendar },
  { name: 'Forms', href: '/forms', icon: FileText },
  { name: 'Business', href: '/business', icon: Building2 },
  { name: 'Analytics', href: '/analytics', icon: BarChart3 },
  { name: 'Settings', href: '/settings', icon: Settings },
];

const Sidebar: React.FC = () => {
  return (
    <div className="hidden lg:fixed lg:inset-y-0 lg:flex lg:w-64 lg:flex-col lg:pt-16">
      <div className="flex min-h-0 flex-1 flex-col bg-white border-r border-gray-200">
        <div className="flex flex-1 flex-col overflow-y-auto pt-5 pb-4">
          <nav className="mt-5 flex-1 space-y-1 px-2">
            {navigation.map((item) => (
              <NavLink
                key={item.name}
                to={item.href}
                className={({ isActive }) =>
                  `group flex items-center px-2 py-2 text-sm font-medium rounded-lg transition-colors ${
                    isActive
                      ? 'bg-primary-50 text-primary-700 border-r-2 border-primary-700'
                      : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
                  }`
                }
              >
                {({ isActive }) => (
                  <>
                    <item.icon
                      className={`mr-3 h-5 w-5 flex-shrink-0 ${
                        isActive ? 'text-primary-500' : 'text-gray-400 group-hover:text-gray-500'
                      }`}
                    />
                    {item.name}
                  </>
                )}
              </NavLink>
            ))}
          </nav>
        </div>
        
        {/* Bottom section */}
        <div className="flex-shrink-0 p-4 border-t border-gray-200">
          <div className="bg-gradient-primary rounded-lg p-4 text-white">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <Bot className="w-6 h-6" />
              </div>
              <div className="ml-3">
                <p className="text-sm font-medium">AI Assistant</p>
                <p className="text-xs opacity-90">115 tools available</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
