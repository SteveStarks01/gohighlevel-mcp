import axios from 'axios';

// Create axios instance with default config
const api = axios.create({
  baseURL: '/api',
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for auth tokens
api.interceptors.request.use(
  (config) => {
    // Add auth token if available
    const token = localStorage.getItem('auth_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized access
      localStorage.removeItem('auth_token');
      window.location.href = '/oauth/callback';
    }
    return Promise.reject(error);
  }
);

// Dashboard API
export const dashboardApi = {
  getOverview: async () => {
    const response = await api.get('/dashboard/overview');
    return response.data;
  },
  
  getContactsSummary: async () => {
    const response = await api.get('/dashboard/contacts/summary');
    return response.data;
  },
  
  getOpportunitiesSummary: async () => {
    const response = await api.get('/dashboard/opportunities/summary');
    return response.data;
  },
  
  getCalendarSummary: async () => {
    const response = await api.get('/dashboard/calendar/summary');
    return response.data;
  },
  
  getChartData: async (chartType: string, period: string = '30d') => {
    const response = await api.get('/dashboard/analytics/chart-data', {
      params: { chart_type: chartType, period }
    });
    return response.data;
  },
};

// Chat API
export const chatApi = {
  sendMessage: async (message: string, conversationId?: string) => {
    const response = await api.post('/chat/message', {
      message,
      conversation_id: conversationId,
    });
    return response.data;
  },
  
  getConversations: async () => {
    const response = await api.get('/chat/conversations');
    return response.data;
  },
  
  getConversationMessages: async (conversationId: string) => {
    const response = await api.get(`/chat/conversations/${conversationId}/messages`);
    return response.data;
  },
  
  getSuggestions: async () => {
    const response = await api.get('/chat/suggestions');
    return response.data;
  },
};

// Auth API
export const authApi = {
  decryptUserData: async (encryptedData: string) => {
    const response = await api.post('/auth/decrypt-user-data', {
      encryptedData,
    });
    return response.data;
  },
  
  getUserContext: async () => {
    const response = await api.get('/auth/user-context');
    return response.data;
  },
  
  logout: async () => {
    const response = await api.post('/auth/logout');
    return response.data;
  },
};

// Contacts API (for future use)
export const contactsApi = {
  getContacts: async (params?: any) => {
    const response = await api.get('/contacts', { params });
    return response.data;
  },
  
  getContact: async (contactId: string) => {
    const response = await api.get(`/contacts/${contactId}`);
    return response.data;
  },
  
  createContact: async (contactData: any) => {
    const response = await api.post('/contacts', contactData);
    return response.data;
  },
  
  updateContact: async (contactId: string, contactData: any) => {
    const response = await api.put(`/contacts/${contactId}`, contactData);
    return response.data;
  },
  
  deleteContact: async (contactId: string) => {
    const response = await api.delete(`/contacts/${contactId}`);
    return response.data;
  },
};

// Opportunities API (for future use)
export const opportunitiesApi = {
  getOpportunities: async (params?: any) => {
    const response = await api.get('/opportunities', { params });
    return response.data;
  },
  
  getOpportunity: async (opportunityId: string) => {
    const response = await api.get(`/opportunities/${opportunityId}`);
    return response.data;
  },
  
  createOpportunity: async (opportunityData: any) => {
    const response = await api.post('/opportunities', opportunityData);
    return response.data;
  },
  
  updateOpportunity: async (opportunityId: string, opportunityData: any) => {
    const response = await api.put(`/opportunities/${opportunityId}`, opportunityData);
    return response.data;
  },
  
  getPipelines: async () => {
    const response = await api.get('/opportunities/pipelines');
    return response.data;
  },
};

// Calendar API (for future use)
export const calendarApi = {
  getCalendars: async () => {
    const response = await api.get('/calendars');
    return response.data;
  },
  
  getAppointments: async (params?: any) => {
    const response = await api.get('/appointments', { params });
    return response.data;
  },
  
  createAppointment: async (appointmentData: any) => {
    const response = await api.post('/appointments', appointmentData);
    return response.data;
  },
  
  getFreeSlots: async (calendarId: string, params?: any) => {
    const response = await api.get(`/calendars/${calendarId}/free-slots`, { params });
    return response.data;
  },
};

export default api;
