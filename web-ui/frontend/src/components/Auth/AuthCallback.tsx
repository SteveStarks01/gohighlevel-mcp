import React, { useEffect, useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { Loader2, CheckCircle, XCircle } from 'lucide-react';
import { authApi } from '../../services/api';

const AuthCallback: React.FC = () => {
  const [status, setStatus] = useState<'loading' | 'success' | 'error'>('loading');
  const [message, setMessage] = useState('Processing authentication...');
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();

  useEffect(() => {
    const handleAuthCallback = async () => {
      try {
        const code = searchParams.get('code');
        const state = searchParams.get('state');
        const error = searchParams.get('error');

        if (error) {
          throw new Error(`Authentication error: ${error}`);
        }

        if (!code) {
          throw new Error('No authorization code received');
        }

        setMessage('Exchanging authorization code for tokens...');

        // The backend will handle the token exchange
        // For now, we'll simulate the process and redirect to dashboard
        
        // In a real implementation, you might:
        // 1. Send the code to your backend
        // 2. Backend exchanges code for tokens
        // 3. Backend returns user context and session info
        // 4. Frontend stores session info and redirects

        // Simulate API call delay
        await new Promise(resolve => setTimeout(resolve, 2000));

        setStatus('success');
        setMessage('Authentication successful! Redirecting to dashboard...');

        // Redirect to dashboard after a short delay
        setTimeout(() => {
          navigate('/dashboard');
        }, 1500);

      } catch (error) {
        console.error('Authentication error:', error);
        setStatus('error');
        setMessage(error instanceof Error ? error.message : 'Authentication failed');
      }
    };

    handleAuthCallback();
  }, [searchParams, navigate]);

  const getStatusIcon = () => {
    switch (status) {
      case 'loading':
        return <Loader2 className="w-8 h-8 text-blue-600 animate-spin" />;
      case 'success':
        return <CheckCircle className="w-8 h-8 text-green-600" />;
      case 'error':
        return <XCircle className="w-8 h-8 text-red-600" />;
    }
  };

  const getStatusColor = () => {
    switch (status) {
      case 'loading':
        return 'text-blue-600';
      case 'success':
        return 'text-green-600';
      case 'error':
        return 'text-red-600';
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
          <div className="text-center">
            {/* Logo */}
            <div className="mx-auto w-16 h-16 bg-gradient-primary rounded-full flex items-center justify-center mb-6">
              <span className="text-white font-bold text-xl">GHL</span>
            </div>

            {/* Status icon */}
            <div className="flex justify-center mb-4">
              {getStatusIcon()}
            </div>

            {/* Title */}
            <h2 className="text-2xl font-bold text-gray-900 mb-2">
              {status === 'loading' && 'Authenticating...'}
              {status === 'success' && 'Success!'}
              {status === 'error' && 'Authentication Failed'}
            </h2>

            {/* Message */}
            <p className={`text-sm ${getStatusColor()} mb-6`}>
              {message}
            </p>

            {/* Progress indicator for loading */}
            {status === 'loading' && (
              <div className="w-full bg-gray-200 rounded-full h-2 mb-4">
                <div className="bg-blue-600 h-2 rounded-full animate-pulse" style={{ width: '60%' }}></div>
              </div>
            )}

            {/* Error actions */}
            {status === 'error' && (
              <div className="space-y-3">
                <button
                  onClick={() => window.location.href = '/'}
                  className="w-full btn btn-primary"
                >
                  Try Again
                </button>
                <button
                  onClick={() => navigate('/dashboard')}
                  className="w-full btn btn-outline"
                >
                  Continue to Dashboard
                </button>
              </div>
            )}

            {/* Success actions */}
            {status === 'success' && (
              <button
                onClick={() => navigate('/dashboard')}
                className="w-full btn btn-primary"
              >
                Continue to Dashboard
              </button>
            )}
          </div>
        </div>

        {/* Footer */}
        <div className="mt-8 text-center">
          <p className="text-xs text-gray-500">
            GoHighLevel MCP AI Assistant
          </p>
        </div>
      </div>
    </div>
  );
};

export default AuthCallback;
