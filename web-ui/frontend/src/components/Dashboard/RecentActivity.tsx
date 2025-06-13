import React from 'react';
import { formatDistanceToNow } from 'date-fns';
import { 
  UserPlus, 
  TrendingUp, 
  Calendar, 
  MessageSquare, 
  Target,
  Users,
  Mail,
  Phone
} from 'lucide-react';

interface Activity {
  type: string;
  description: string;
  timestamp: string;
  icon?: string;
}

interface RecentActivityProps {
  activities: Activity[];
}

const RecentActivity: React.FC<RecentActivityProps> = ({ activities }) => {
  const getActivityIcon = (type: string) => {
    const iconMap = {
      'contact_created': UserPlus,
      'opportunity_updated': TrendingUp,
      'appointment_scheduled': Calendar,
      'message_sent': MessageSquare,
      'opportunity_created': Target,
      'contact_updated': Users,
      'email_sent': Mail,
      'call_logged': Phone,
    };
    
    return iconMap[type as keyof typeof iconMap] || UserPlus;
  };

  const getActivityColor = (type: string) => {
    const colorMap = {
      'contact_created': 'text-green-600 bg-green-50',
      'opportunity_updated': 'text-blue-600 bg-blue-50',
      'appointment_scheduled': 'text-purple-600 bg-purple-50',
      'message_sent': 'text-orange-600 bg-orange-50',
      'opportunity_created': 'text-indigo-600 bg-indigo-50',
      'contact_updated': 'text-gray-600 bg-gray-50',
      'email_sent': 'text-cyan-600 bg-cyan-50',
      'call_logged': 'text-pink-600 bg-pink-50',
    };
    
    return colorMap[type as keyof typeof colorMap] || 'text-gray-600 bg-gray-50';
  };

  // Mock data if no activities provided
  const defaultActivities = [
    {
      type: 'contact_created',
      description: 'New contact: John Smith added to the system',
      timestamp: new Date().toISOString(),
    },
    {
      type: 'opportunity_updated',
      description: 'ABC Corp deal moved to "Proposal" stage',
      timestamp: new Date(Date.now() - 15 * 60 * 1000).toISOString(),
    },
    {
      type: 'appointment_scheduled',
      description: 'Sales call scheduled with Sarah Johnson',
      timestamp: new Date(Date.now() - 30 * 60 * 1000).toISOString(),
    },
    {
      type: 'message_sent',
      description: 'Follow-up email sent to 5 leads',
      timestamp: new Date(Date.now() - 45 * 60 * 1000).toISOString(),
    },
    {
      type: 'opportunity_created',
      description: 'New opportunity: Tech Solutions Project ($25,000)',
      timestamp: new Date(Date.now() - 60 * 60 * 1000).toISOString(),
    },
  ];

  const displayActivities = activities.length > 0 ? activities : defaultActivities;

  return (
    <div className="card">
      <div className="card-header">
        <h3 className="text-lg font-semibold text-gray-900">Recent Activity</h3>
        <p className="text-sm text-gray-500 mt-1">
          Latest updates from your GoHighLevel account
        </p>
      </div>
      <div className="card-body p-0">
        <div className="flow-root">
          <ul className="divide-y divide-gray-200">
            {displayActivities.slice(0, 8).map((activity, index) => {
              const Icon = getActivityIcon(activity.type);
              const colorClasses = getActivityColor(activity.type);
              
              return (
                <li key={index} className="px-6 py-4 hover:bg-gray-50 transition-colors">
                  <div className="flex items-start space-x-3">
                    <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${colorClasses}`}>
                      <Icon className="w-4 h-4" />
                    </div>
                    <div className="flex-1 min-w-0">
                      <p className="text-sm text-gray-900 font-medium">
                        {activity.description}
                      </p>
                      <p className="text-xs text-gray-500 mt-1">
                        {formatDistanceToNow(new Date(activity.timestamp), { addSuffix: true })}
                      </p>
                    </div>
                  </div>
                </li>
              );
            })}
          </ul>
        </div>
        
        {displayActivities.length > 8 && (
          <div className="card-footer">
            <button className="w-full text-center text-sm text-primary-600 hover:text-primary-700 font-medium">
              View all activity
            </button>
          </div>
        )}
        
        {displayActivities.length === 0 && (
          <div className="px-6 py-8 text-center">
            <div className="text-gray-400 mb-2">
              <Calendar className="w-8 h-8 mx-auto" />
            </div>
            <p className="text-sm text-gray-500">No recent activity</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default RecentActivity;
