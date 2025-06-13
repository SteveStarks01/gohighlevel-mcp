import { useEffect, useRef, useState, useCallback } from 'react';
import { io, Socket } from 'socket.io-client';

interface UseWebSocketOptions {
  url: string;
  onMessage?: (data: any) => void;
  onConnect?: () => void;
  onDisconnect?: () => void;
  onError?: (error: any) => void;
  autoReconnect?: boolean;
  reconnectAttempts?: number;
  reconnectDelay?: number;
}

interface UseWebSocketReturn {
  socket: Socket | null;
  isConnected: boolean;
  sendMessage: (data: any) => void;
  disconnect: () => void;
  reconnect: () => void;
}

export const useWebSocket = (options: UseWebSocketOptions): UseWebSocketReturn => {
  const {
    url,
    onMessage,
    onConnect,
    onDisconnect,
    onError,
    autoReconnect = true,
    reconnectAttempts = 5,
    reconnectDelay = 1000,
  } = options;

  const [isConnected, setIsConnected] = useState(false);
  const [reconnectCount, setReconnectCount] = useState(0);
  const socketRef = useRef<Socket | null>(null);
  const reconnectTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  const connect = useCallback(() => {
    try {
      // Convert WebSocket URL to Socket.IO URL
      const socketUrl = url.replace('ws://', 'http://').replace('wss://', 'https://');
      const baseUrl = socketUrl.split('/ws/')[0];
      
      // Create Socket.IO connection
      const socket = io(baseUrl, {
        transports: ['websocket', 'polling'],
        timeout: 10000,
        forceNew: true,
      });

      socketRef.current = socket;

      socket.on('connect', () => {
        console.log('WebSocket connected');
        setIsConnected(true);
        setReconnectCount(0);
        onConnect?.();
      });

      socket.on('disconnect', (reason) => {
        console.log('WebSocket disconnected:', reason);
        setIsConnected(false);
        onDisconnect?.();

        // Auto-reconnect logic
        if (autoReconnect && reconnectCount < reconnectAttempts) {
          reconnectTimeoutRef.current = setTimeout(() => {
            setReconnectCount(prev => prev + 1);
            connect();
          }, reconnectDelay * Math.pow(2, reconnectCount)); // Exponential backoff
        }
      });

      socket.on('message', (data) => {
        onMessage?.(data);
      });

      socket.on('chat_message', (data) => {
        onMessage?.(data);
      });

      socket.on('error', (error) => {
        console.error('WebSocket error:', error);
        onError?.(error);
      });

      socket.on('connect_error', (error) => {
        console.error('WebSocket connection error:', error);
        setIsConnected(false);
        onError?.(error);
      });

    } catch (error) {
      console.error('Failed to create WebSocket connection:', error);
      onError?.(error);
    }
  }, [url, onMessage, onConnect, onDisconnect, onError, autoReconnect, reconnectAttempts, reconnectDelay, reconnectCount]);

  const sendMessage = useCallback((data: any) => {
    if (socketRef.current && isConnected) {
      socketRef.current.emit('chat_message', data);
    } else {
      console.warn('WebSocket not connected. Message not sent:', data);
    }
  }, [isConnected]);

  const disconnect = useCallback(() => {
    if (reconnectTimeoutRef.current) {
      clearTimeout(reconnectTimeoutRef.current);
      reconnectTimeoutRef.current = null;
    }
    
    if (socketRef.current) {
      socketRef.current.disconnect();
      socketRef.current = null;
    }
    
    setIsConnected(false);
  }, []);

  const reconnect = useCallback(() => {
    disconnect();
    setReconnectCount(0);
    connect();
  }, [disconnect, connect]);

  useEffect(() => {
    connect();

    return () => {
      disconnect();
    };
  }, [connect, disconnect]);

  return {
    socket: socketRef.current,
    isConnected,
    sendMessage,
    disconnect,
    reconnect,
  };
};

// Alternative WebSocket hook for native WebSocket API
export const useNativeWebSocket = (options: UseWebSocketOptions): UseWebSocketReturn => {
  const {
    url,
    onMessage,
    onConnect,
    onDisconnect,
    onError,
    autoReconnect = true,
    reconnectAttempts = 5,
    reconnectDelay = 1000,
  } = options;

  const [isConnected, setIsConnected] = useState(false);
  const [reconnectCount, setReconnectCount] = useState(0);
  const wsRef = useRef<WebSocket | null>(null);
  const reconnectTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  const connect = useCallback(() => {
    try {
      const ws = new WebSocket(url);
      wsRef.current = ws;

      ws.onopen = () => {
        console.log('WebSocket connected');
        setIsConnected(true);
        setReconnectCount(0);
        onConnect?.();
      };

      ws.onclose = (event) => {
        console.log('WebSocket disconnected:', event.code, event.reason);
        setIsConnected(false);
        onDisconnect?.();

        // Auto-reconnect logic
        if (autoReconnect && reconnectCount < reconnectAttempts && event.code !== 1000) {
          reconnectTimeoutRef.current = setTimeout(() => {
            setReconnectCount(prev => prev + 1);
            connect();
          }, reconnectDelay * Math.pow(2, reconnectCount));
        }
      };

      ws.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          onMessage?.(data);
        } catch (error) {
          console.error('Failed to parse WebSocket message:', error);
          onMessage?.(event.data);
        }
      };

      ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        onError?.(error);
      };

    } catch (error) {
      console.error('Failed to create WebSocket connection:', error);
      onError?.(error);
    }
  }, [url, onMessage, onConnect, onDisconnect, onError, autoReconnect, reconnectAttempts, reconnectDelay, reconnectCount]);

  const sendMessage = useCallback((data: any) => {
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify(data));
    } else {
      console.warn('WebSocket not connected. Message not sent:', data);
    }
  }, []);

  const disconnect = useCallback(() => {
    if (reconnectTimeoutRef.current) {
      clearTimeout(reconnectTimeoutRef.current);
      reconnectTimeoutRef.current = null;
    }
    
    if (wsRef.current) {
      wsRef.current.close(1000, 'User disconnected');
      wsRef.current = null;
    }
    
    setIsConnected(false);
  }, []);

  const reconnect = useCallback(() => {
    disconnect();
    setReconnectCount(0);
    connect();
  }, [disconnect, connect]);

  useEffect(() => {
    connect();

    return () => {
      disconnect();
    };
  }, [connect, disconnect]);

  return {
    socket: wsRef.current as any,
    isConnected,
    sendMessage,
    disconnect,
    reconnect,
  };
};
