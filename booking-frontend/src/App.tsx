import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { AuthProvider } from './context/AuthContext';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import Treatments from './pages/Treatments';
import BookingPage from './pages/BookingPage';
import MyAccount from './pages/MyAccount';
import MyBookings from './pages/MyBookings';
import MyFavorites from './pages/MyFavorites';
import Support from './pages/Support';
import './App.css';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <AuthProvider>
        <Router>
          <div className="app">
            <Header />
            <main className="main-content">
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/treatments" element={<Treatments />} />
                <Route path="/categories/:categoryId" element={<Treatments />} />
                <Route path="/treatment/:treatmentId" element={<BookingPage />} />
                <Route path="/account" element={<MyAccount />} />
                <Route path="/account/bookings" element={<MyBookings />} />
                <Route path="/favorites" element={<MyFavorites />} />
                <Route path="/support" element={<Support />} />
              </Routes>
            </main>
            <Footer />
          </div>
        </Router>
      </AuthProvider>
    </QueryClientProvider>
  );
}

export default App;
