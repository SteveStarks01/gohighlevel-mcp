import React from 'react';
import { useQuery } from '@tanstack/react-query';
import KPICards from './KPICards';
import ChartSection from './ChartSection';
import RecentActivity from './RecentActivity';
import ChatInterface from '../Chat/ChatInterface';
import { dashboardApi } from '../../services/api';

const Dashboard: React.FC = () => {
  // Fetch dashboard data
  const { data: dashboardData, isLoading, error } = useQuery({
    queryKey: ['dashboard-overview'],
    queryFn: dashboardApi.getOverview,
    refetchInterval: 30000, // Refetch every 30 seconds
  });

  if (isLoading) {
    return (
      <div className="animate-pulse">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          {[...Array(4)].map((_, i) => (
            <div key={i} className="card">
              <div className="card-body">
                <div className="h-4 bg-gray-200 rounded w-3/4 mb-2"></div>
                <div className="h-8 bg-gray-200 rounded w-1/2"></div>
              </div>
            </div>
          ))}
        </div>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
          <div className="card">
            <div className="card-body">
              <div className="h-64 bg-gray-200 rounded"></div>
            </div>
          </div>
          <div className="card">
            <div className="card-body">
              <div className="h-64 bg-gray-200 rounded"></div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="card">
        <div className="card-body text-center py-12">
          <div className="text-red-500 mb-4">
            <svg className="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z" />
            </svg>
          </div>
          <h3 className="text-lg font-medium text-gray-900 mb-2">Failed to load dashboard</h3>
          <p className="text-gray-500">Please try refreshing the page or contact support if the problem persists.</p>
        </div>
      </div>
    );
  }

  const kpis = dashboardData?.data?.kpis || {};
  const recentActivity = dashboardData?.data?.recent_activity || [];
  const pipelineSummary = dashboardData?.data?.pipeline_summary || {};

  return (
    <div className="space-y-8">
      {/* Page header */}
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Dashboard</h1>
        <p className="text-gray-600 mt-1">
          Welcome back! Here's what's happening with your GoHighLevel account.
        </p>
      </div>

      {/* KPI Cards */}
      <KPICards kpis={kpis} />

      {/* Charts and Recent Activity */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Charts Section - Takes 2/3 of the width */}
        <div className="lg:col-span-2">
          <ChartSection pipelineSummary={pipelineSummary} />
        </div>

        {/* Recent Activity - Takes 1/3 of the width */}
        <div>
          <RecentActivity activities={recentActivity} />
        </div>
      </div>

      {/* AI Chat Interface */}
      <div className="mt-8">
        <div className="card">
          <div className="card-header">
            <h2 className="text-lg font-semibold text-gray-900 flex items-center">
              <svg className="w-5 h-5 mr-2 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
              </svg>
              AI Assistant
            </h2>
            <p className="text-sm text-gray-500 mt-1">
              Ask questions about your data or request actions using natural language
            </p>
          </div>
          <div className="card-body p-0">
            <ChatInterface />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
