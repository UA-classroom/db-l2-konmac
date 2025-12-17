import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { getTreatments, getBusinessLocations } from '../services/api';
import type { Treatment, BusinessLocation } from '../types';
import { Calendar, Clock, MapPin, AlertCircle } from 'lucide-react';
import './MyBookings.css';

interface DemoBooking {
  booking_id: number;
  location_id: number;
  treatment_id: number;
  booked_date: string;
  time_start: string;
  time_stop: string;
  notes?: string;
  booking_status: number;
}

export default function MyBookings() {
  const { user } = useAuth();
  const [treatments, setTreatments] = useState<Treatment[]>([]);
  const [locations, setLocations] = useState<BusinessLocation[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Demo bookings for Anna Andersson (customer_id: 1)
  const demoBookings: DemoBooking[] = [
    {
      booking_id: 7,
      location_id: 2,
      treatment_id: 10,
      booked_date: '2025-12-25',
      time_start: '09:00:00',
      time_stop: '10:00:00',
      booking_status: 1,
    },
    {
      booking_id: 1,
      location_id: 1,
      treatment_id: 1,
      booked_date: '2025-12-20',
      time_start: '10:00:00',
      time_stop: '11:00:00',
      notes: 'Vill ha lugg',
      booking_status: 1,
    },
    {
      booking_id: 15,
      location_id: 3,
      treatment_id: 24,
      booked_date: '2025-11-15',
      time_start: '14:00:00',
      time_stop: '15:30:00',
      booking_status: 1,
    },
  ];

  useEffect(() => {
    fetchData();
  }, [user]);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [treatmentsRes, locationsRes] = await Promise.all([
        getTreatments(),
        getBusinessLocations(),
      ]);

      const treatmentsData = treatmentsRes.data.treatments || treatmentsRes.data || [];
      const locationsData = locationsRes.data.business_locations || locationsRes.data || [];

      setTreatments(Array.isArray(treatmentsData) ? treatmentsData : []);
      setLocations(Array.isArray(locationsData) ? locationsData : []);
      setError(null);
    } catch (err: any) {
      console.error('Error fetching data:', err);
      setError(err.response?.data?.detail || err.message || 'Failed to fetch data');
    } finally {
      setLoading(false);
    }
  };

  const getTreatmentById = (id: number) => treatments.find(t => t.treatment_id === id);
  const getLocationById = (id: number) => locations.find(l => l.location_id === id);

  const upcomingBookings = demoBookings.filter(b => new Date(b.booked_date) >= new Date());
  const pastBookings = demoBookings.filter(b => new Date(b.booked_date) < new Date());

  const formatDate = (dateStr: string) => {
    const date = new Date(dateStr);
    return date.toLocaleDateString('sv-SE', { year: 'numeric', month: 'long', day: 'numeric' });
  };

  const formatTime = (timeStr: string) => {
    return timeStr.substring(0, 5);
  };

  const renderBooking = (booking: DemoBooking) => {
    const treatment = getTreatmentById(booking.treatment_id);
    const location = getLocationById(booking.location_id);

    return (
      <div key={booking.booking_id} className="booking-card card">
        <div className="booking-header">
          <div className="booking-date">
            <Calendar size={20} />
            <div>
              <div className="date-text">{formatDate(booking.booked_date)}</div>
              <div className="time-text">
                <Clock size={16} />
                {formatTime(booking.time_start)} - {formatTime(booking.time_stop)}
              </div>
            </div>
          </div>
          <div className={`booking-status status-${booking.booking_status}`}>
            {booking.booking_status === 1 ? 'Bekräftad' :
             booking.booking_status === 2 ? 'Avbokad' : 'Väntande'}
          </div>
        </div>

        <div className="booking-content">
          <h3>{treatment?.treatment_name || 'Behandling'}</h3>
          {treatment?.treatment_description && (
            <p className="treatment-desc">{treatment.treatment_description}</p>
          )}

          {location && (
            <div className="location-info">
              <MapPin size={16} />
              <span>{location.street_address}, {location.city}</span>
            </div>
          )}

          {booking.notes && (
            <div className="booking-notes">
              <AlertCircle size={16} />
              <span>Notering: {booking.notes}</span>
            </div>
          )}
        </div>

        <div className="booking-actions">
          <Link to={`/treatment/${booking.treatment_id}`} className="btn btn-secondary">
            Visa detaljer
          </Link>
          {booking.booking_status === 1 && (
            <button className="btn btn-outline">Avboka</button>
          )}
        </div>
      </div>
    );
  };

  return (
    <div className="my-bookings-page">
      <div className="container">
        <div className="page-header">
          <h1>Mina bokningar</h1>
          <p>Hantera dina kommande och tidigare bokningar</p>
        </div>

        {loading && <div className="loading">Laddar bokningar...</div>}
        {error && <div className="error">{error}</div>}

        {!loading && !error && demoBookings.length === 0 && (
          <div className="empty-state">
            <Calendar size={48} />
            <h3>Inga bokningar ännu</h3>
            <p>När du bokar behandlingar kommer de att visas här</p>
            <Link to="/treatments" className="btn btn-primary">
              Boka behandling
            </Link>
          </div>
        )}

        {!loading && !error && demoBookings.length > 0 && (
          <>
            {upcomingBookings.length > 0 && (
              <section className="bookings-section">
                <h2>Kommande bokningar</h2>
                <div className="bookings-list">
                  {upcomingBookings.map(renderBooking)}
                </div>
              </section>
            )}

            {pastBookings.length > 0 && (
              <section className="bookings-section">
                <h2>Tidigare bokningar</h2>
                <div className="bookings-list">
                  {pastBookings.map(renderBooking)}
                </div>
              </section>
            )}
          </>
        )}
      </div>
    </div>
  );
}
