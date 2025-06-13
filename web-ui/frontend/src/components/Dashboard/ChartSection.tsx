import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
} from 'chart.js';
import { Bar, Doughnut } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement
);

interface PipelineStage {
  name: string;
  count: number;
  value: number;
}

interface PipelineSummary {
  stages?: PipelineStage[];
}

interface ChartSectionProps {
  pipelineSummary: PipelineSummary;
}

const ChartSection: React.FC<ChartSectionProps> = ({ pipelineSummary }) => {
  const stages = pipelineSummary.stages || [
    { name: 'Lead', count: 25, value: 50000 },
    { name: 'Qualified', count: 18, value: 75000 },
    { name: 'Proposal', count: 12, value: 85000 },
    { name: 'Closed Won', count: 8, value: 35000 }
  ];

  // Pipeline Value Chart Data
  const pipelineChartData = {
    labels: stages.map(stage => stage.name),
    datasets: [
      {
        label: 'Pipeline Value ($)',
        data: stages.map(stage => stage.value),
        backgroundColor: [
          'rgba(239, 68, 68, 0.8)',   // Red
          'rgba(245, 158, 11, 0.8)',  // Orange
          'rgba(59, 130, 246, 0.8)',  // Blue
          'rgba(34, 197, 94, 0.8)',   // Green
        ],
        borderColor: [
          'rgba(239, 68, 68, 1)',
          'rgba(245, 158, 11, 1)',
          'rgba(59, 130, 246, 1)',
          'rgba(34, 197, 94, 1)',
        ],
        borderWidth: 1,
        borderRadius: 8,
      },
    ],
  };

  // Opportunity Count Doughnut Chart Data
  const opportunityChartData = {
    labels: stages.map(stage => stage.name),
    datasets: [
      {
        label: 'Opportunities',
        data: stages.map(stage => stage.count),
        backgroundColor: [
          'rgba(239, 68, 68, 0.8)',
          'rgba(245, 158, 11, 0.8)',
          'rgba(59, 130, 246, 0.8)',
          'rgba(34, 197, 94, 0.8)',
        ],
        borderColor: [
          'rgba(239, 68, 68, 1)',
          'rgba(245, 158, 11, 1)',
          'rgba(59, 130, 246, 1)',
          'rgba(34, 197, 94, 1)',
        ],
        borderWidth: 2,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top' as const,
      },
      tooltip: {
        callbacks: {
          label: function(context: any) {
            const label = context.dataset.label || '';
            const value = context.parsed.y || context.parsed;
            if (label.includes('Value')) {
              return `${label}: $${value.toLocaleString()}`;
            }
            return `${label}: ${value}`;
          }
        }
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          callback: function(value: any) {
            return '$' + value.toLocaleString();
          }
        }
      }
    }
  };

  const doughnutOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'bottom' as const,
      },
      tooltip: {
        callbacks: {
          label: function(context: any) {
            const label = context.label || '';
            const value = context.parsed;
            const total = context.dataset.data.reduce((a: number, b: number) => a + b, 0);
            const percentage = ((value / total) * 100).toFixed(1);
            return `${label}: ${value} (${percentage}%)`;
          }
        }
      }
    }
  };

  return (
    <div className="space-y-6">
      {/* Pipeline Value Chart */}
      <div className="card">
        <div className="card-header">
          <h3 className="text-lg font-semibold text-gray-900">Pipeline Value by Stage</h3>
          <p className="text-sm text-gray-500 mt-1">
            Total value of opportunities in each pipeline stage
          </p>
        </div>
        <div className="card-body">
          <div className="chart-container">
            <Bar data={pipelineChartData} options={chartOptions} />
          </div>
        </div>
      </div>

      {/* Opportunity Distribution Chart */}
      <div className="card">
        <div className="card-header">
          <h3 className="text-lg font-semibold text-gray-900">Opportunity Distribution</h3>
          <p className="text-sm text-gray-500 mt-1">
            Number of opportunities in each pipeline stage
          </p>
        </div>
        <div className="card-body">
          <div className="chart-container">
            <Doughnut data={opportunityChartData} options={doughnutOptions} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChartSection;
