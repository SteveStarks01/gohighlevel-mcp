import React from 'react';
import { Users, Target, Calendar, DollarSign, TrendingUp, TrendingDown } from 'lucide-react';

interface KPIData {
  total_contacts?: number;
  total_opportunities?: number;
  total_opportunity_value?: number;
  appointments_today?: number;
  active_campaigns?: number;
  conversion_rate?: number;
}

interface KPICardsProps {
  kpis: KPIData;
}

const KPICards: React.FC<KPICardsProps> = ({ kpis }) => {
  const formatCurrency = (value: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(value);
  };

  const formatNumber = (value: number) => {
    return new Intl.NumberFormat('en-US').format(value);
  };

  const cards = [
    {
      title: 'Total Contacts',
      value: formatNumber(kpis.total_contacts || 0),
      icon: Users,
      color: 'blue',
      change: '+12%',
      changeType: 'increase',
      description: 'vs last month'
    },
    {
      title: 'Opportunities',
      value: formatNumber(kpis.total_opportunities || 0),
      icon: Target,
      color: 'green',
      change: '+8%',
      changeType: 'increase',
      description: 'vs last month'
    },
    {
      title: 'Pipeline Value',
      value: formatCurrency(kpis.total_opportunity_value || 0),
      icon: DollarSign,
      color: 'purple',
      change: '+15%',
      changeType: 'increase',
      description: 'vs last month'
    },
    {
      title: 'Today\'s Appointments',
      value: formatNumber(kpis.appointments_today || 0),
      icon: Calendar,
      color: 'orange',
      change: '-2%',
      changeType: 'decrease',
      description: 'vs yesterday'
    }
  ];

  const getColorClasses = (color: string) => {
    const colorMap = {
      blue: {
        bg: 'bg-blue-50',
        icon: 'text-blue-600',
        text: 'text-blue-600'
      },
      green: {
        bg: 'bg-green-50',
        icon: 'text-green-600',
        text: 'text-green-600'
      },
      purple: {
        bg: 'bg-purple-50',
        icon: 'text-purple-600',
        text: 'text-purple-600'
      },
      orange: {
        bg: 'bg-orange-50',
        icon: 'text-orange-600',
        text: 'text-orange-600'
      }
    };
    return colorMap[color as keyof typeof colorMap] || colorMap.blue;
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {cards.map((card, index) => {
        const colors = getColorClasses(card.color);
        const Icon = card.icon;
        const ChangeIcon = card.changeType === 'increase' ? TrendingUp : TrendingDown;
        
        return (
          <div key={index} className="card hover:shadow-medium transition-shadow duration-200">
            <div className="card-body">
              <div className="flex items-center justify-between">
                <div className="flex-1">
                  <p className="text-sm font-medium text-gray-600 mb-1">
                    {card.title}
                  </p>
                  <p className="text-2xl font-bold text-gray-900 mb-2">
                    {card.value}
                  </p>
                  <div className="flex items-center text-sm">
                    <ChangeIcon 
                      className={`w-4 h-4 mr-1 ${
                        card.changeType === 'increase' ? 'text-green-500' : 'text-red-500'
                      }`} 
                    />
                    <span 
                      className={`font-medium ${
                        card.changeType === 'increase' ? 'text-green-600' : 'text-red-600'
                      }`}
                    >
                      {card.change}
                    </span>
                    <span className="text-gray-500 ml-1">
                      {card.description}
                    </span>
                  </div>
                </div>
                <div className={`p-3 rounded-lg ${colors.bg}`}>
                  <Icon className={`w-6 h-6 ${colors.icon}`} />
                </div>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default KPICards;
