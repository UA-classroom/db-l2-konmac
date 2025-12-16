import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { getTreatments } from '../services/api';
import type { Treatment } from '../types';
import { Calendar, Heart, User, Mail, Phone, MapPin, Clock } from 'lucide-react';
import './MyAccount.css';

export default function MyAccount() {
  const { user } = useAuth();
  const [favorites, setFavorites] = useState<number[]>([]);
  const [treatments, setTreatments] = useState<Treatment[]>([]);
  const [loading, setLoading] = useState(true);

  // Demo bookings for the user
  const demoBookings = [
    {
      booking_id: 7,
      treatment_name: 'Gellack Händer',
      booked_date: '2025-12-25',
      time_start: '09:00:00',
    },
    {
      booking_id: 1,
      treatment_name: 'Damklippning',
      booked_date: '2025-12-20',
      time_start: '10:00:00',
    },
  ];

  useEffect(() => {
    // Load favorites from localStorage
    const storedFavorites = localStorage.getItem('favorites');
    if (storedFavorites) {
      setFavorites(JSON.parse(storedFavorites));
    }

    fetchTreatments();
  }, []);

  const fetchTreatments = async () => {
    try {
      setLoading(true);
      const response = await getTreatments();
      const treatmentsData = response.data.treatments || response.data || [];
      setTreatments(Array.isArray(treatmentsData) ? treatmentsData : []);
    } catch (err) {
      console.error('Error fetching treatments:', err);
    } finally {
      setLoading(false);
    }
  };

  const favoriteTreatments = treatments.filter(t => favorites.includes(t.treatment_id)).slice(0, 3);
  const upcomingBookings = demoBookings.filter(b => new Date(b.booked_date) >= new Date()).slice(0, 3);

  const formatDate = (dateStr: string) => {
    const date = new Date(dateStr);
    return date.toLocaleDateString('sv-SE', { year: 'numeric', month: 'long', day: 'numeric' });
  };

  const formatTime = (timeStr: string) => {
    return timeStr.substring(0, 5);
  };

  return (
    <div className="my-account-page">
      <div className="container">
        <div className="account-header">
          <div className="user-avatar">
            <User size={48} />
          </div>
          <div className="user-info-header">
            <h1>{user?.first_name} {user?.last_name}</h1>
            <p className="user-subtitle">Välkommen tillbaka!</p>
          </div>
        </div>

        <div className="user-details-card card">
          <h2>Mina uppgifter</h2>
          <div className="user-details-grid">
            <div className="detail-item">
              <User size={20} />
              <div>
                <span className="detail-label">Namn</span>
                <span className="detail-value">{user?.first_name} {user?.last_name}</span>
              </div>
            </div>
            <div className="detail-item">
              <Mail size={20} />
              <div>
                <span className="detail-label">Email</span>
                <span className="detail-value">{user?.email}</span>
              </div>
            </div>
            <div className="detail-item">
              <Phone size={20} />
              <div>
                <span className="detail-label">Telefon</span>
                <span className="detail-value">{user?.phone_number}</span>
              </div>
            </div>
            <div className="detail-item">
              <MapPin size={20} />
              <div>
                <span className="detail-label">Kund-ID</span>
                <span className="detail-value">#{user?.customer_id}</span>
              </div>
            </div>
          </div>
        </div>

        <div className="account-overview">
          <div className="overview-section card">
            <div className="section-header">
              <div className="section-title">
                <Calendar size={24} />
                <h2>Kommande bokningar</h2>
              </div>
              <Link to="/account/bookings" className="view-all-link">
                Visa alla →
              </Link>
            </div>

            {upcomingBookings.length === 0 ? (
              <div className="empty-state-small">
                <p>Inga kommande bokningar</p>
                <Link to="/treatments" className="btn btn-primary btn-sm">
                  Boka behandling
                </Link>
              </div>
            ) : (
              <div className="bookings-preview">
                {upcomingBookings.map((booking) => (
                  <div key={booking.booking_id} className="booking-preview-item">
                    <div className="booking-preview-icon">
                      <Calendar size={20} />
                    </div>
                    <div className="booking-preview-content">
                      <h4>{booking.treatment_name}</h4>
                      <div className="booking-preview-meta">
                        <span>{formatDate(booking.booked_date)}</span>
                        <span className="separator">•</span>
                        <span><Clock size={14} /> {formatTime(booking.time_start)}</span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

          <div className="overview-section card">
            <div className="section-header">
              <div className="section-title">
                <Heart size={24} />
                <h2>Mina favoriter</h2>
              </div>
              <Link to="/favorites" className="view-all-link">
                Visa alla →
              </Link>
            </div>

            {loading ? (
              <div className="loading-small">Laddar...</div>
            ) : favoriteTreatments.length === 0 ? (
              <div className="empty-state-small">
                <p>Inga favoriter sparade</p>
                <Link to="/treatments" className="btn btn-secondary btn-sm">
                  Utforska behandlingar
                </Link>
              </div>
            ) : (
              <div className="favorites-preview">
                {favoriteTreatments.map((treatment) => (
                  <div key={treatment.treatment_id} className="favorite-preview-item">
                    <Heart size={16} className="favorite-icon" />
                    <div className="favorite-preview-content">
                      <h4>{treatment.treatment_name}</h4>
                      <span className="treatment-duration">
                        <Clock size={14} /> {treatment.time_duration} min
                      </span>
                    </div>
                    <Link
                      to={`/treatment/${treatment.treatment_id}`}
                      className="btn btn-sm btn-outline"
                    >
                      Boka
                    </Link>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
