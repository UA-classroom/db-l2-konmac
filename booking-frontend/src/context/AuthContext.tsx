import { createContext, useContext, useState, type ReactNode } from 'react';

interface DemoUser {
  customer_id: number;
  first_name: string;
  last_name: string;
  email: string;
  phone_number: string;
}

interface AuthContextType {
  user: DemoUser | null;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider = ({ children }: AuthProviderProps) => {
  // Demo user - automatically logged in
  const [user] = useState<DemoUser>({
    customer_id: 1,
    first_name: 'Anna',
    last_name: 'Andersson',
    email: 'anna.andersson@email.se',
    phone_number: '070-1234567',
  });

  const [isAuthenticated] = useState(true);

  return (
    <AuthContext.Provider value={{ user, isAuthenticated }}>
      {children}
    </AuthContext.Provider>
  );
};
