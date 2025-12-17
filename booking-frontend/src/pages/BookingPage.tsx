import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getTreatments, getBusinesses, getBusinessLocations, createBooking } from '../services/api';
import type { Treatment, Business, BusinessLocation } from '../types';
import { Clock, MapPin, DollarSign } from 'lucide-react';
import './BookingPage.css';

export default function BookingPage() {
  const { treatmentId } = useParams();
  const navigate = useNavigate();
  const [treatment, setTreatment] = useState<Treatment | null>(null);
  const [businesses, setBusinesses] = useState<Business[]>([]);
  const [locations, setLocations] = useState<BusinessLocation[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);

  const [formData, setFormData] = useState({
    locationId: '',
    businessId: '',
    date: '',
    time: '',
    notes: '',
  });

  useEffect(() => {
    fetchData();
  }, [treatmentId]);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [treatmentsRes, businessesRes, locationsRes] = await Promise.all([
        getTreatments(),
        getBusinesses(),
        getBusinessLocations(),
      ]);

      const treatmentsData = treatmentsRes.data.treatments || [];
      const businessesData = businessesRes.data.businesses || [];
      const locationsData = locationsRes.data.business_locations || [];

      const foundTreatment = treatmentsData.find(
        (t: Treatment) => t.treatment_id === parseInt(treatmentId || '0')
      );

      setTreatment(foundTreatment || null);
      setBusinesses(businessesData);
      setLocations(locationsData);
      setError(null);
    } catch (err: any) {
      console.error('Error fetching data:', err);
      setError('Failed to load booking information');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!treatment || !formData.locationId || !formData.businessId || !formData.date || !formData.time) {
      setError('Vänligen fyll i alla obligatoriska fält');
      return;
    }

    try {
      setSubmitting(true);
      setError(null);

      const timeEnd = new Date(`2000-01-01T${formData.time}`);
      timeEnd.setMinutes(timeEnd.getMinutes() + treatment.time_duration);
      const timeEndStr = timeEnd.toTimeString().slice(0, 5);

      await createBooking({
        location_id: parseInt(formData.locationId),
        treatment_id: treatment.treatment_id,
        customer_id: 1, // This should come from authentication
        business_id: parseInt(formData.businessId),
        booked_date: formData.date,
        time_start: formData.time,
        time_stop: timeEndStr,
        notes: formData.notes,
        booking_status: 1,
        payment_confirmed: false,
      });

      alert('Bokning skapad!');
      navigate('/account/bookings');
    } catch (err: any) {
      console.error('Error creating booking:', err);
      setError(err.response?.data?.detail || 'Failed to create booking');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return <div className="loading">Laddar...</div>;
  }

  if (!treatment) {
    return (
      <div className="container" style={{ padding: '3rem 0' }}>
        <div className="error">Behandling hittades inte</div>
      </div>
    );
  }

  const selectedLocation = locations.find(
    (l) => l.location_id === parseInt(formData.locationId)
  );

  return (
    <div className="booking-page">
      <div className="container">
        <div className="booking-content">
          <div className="booking-info">
            <h1>Boka {treatment.treatment_name}</h1>

            <div className="treatment-details card">
              <img
                src={treatment.image_url || 'https://images.unsplash.com/photo-1519415387722-a1c3bbef716c?w=600'}
                alt={treatment.treatment_name}
              />
              <div className="details-content">
                <h2>{treatment.treatment_name}</h2>
                <p>{treatment.treatment_description}</p>
                <div className="detail-items">
                  <div className="detail-item">
                    <Clock size={20} />
                    <span>{treatment.time_duration} minuter</span>
                  </div>
                  <div className="detail-item">
                    <DollarSign size={20} />
                    <span>{treatment.price} kr</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="booking-form-section">
            <form onSubmit={handleSubmit} className="booking-form card">
              <h3>Bokningsdetaljer</h3>

              {error && <div className="error">{error}</div>}

              <div className="form-group">
                <label>Välj verksamhet *</label>
                <select
                  value={formData.businessId}
                  onChange={(e) => setFormData({ ...formData, businessId: e.target.value })}
                  required
                >
                  <option value="">Välj verksamhet</option>
                  {businesses.map((business) => (
                    <option key={business.business_id} value={business.business_id}>
                      {business.business_name}
                    </option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label>Välj plats *</label>
                <select
                  value={formData.locationId}
                  onChange={(e) => setFormData({ ...formData, locationId: e.target.value })}
                  required
                >
                  <option value="">Välj plats</option>
                  {locations.map((location) => (
                    <option key={location.location_id} value={location.location_id}>
                      {location.street_address}, {location.city}
                    </option>
                  ))}
                </select>
                {selectedLocation && (
                  <div className="location-info">
                    <MapPin size={16} />
                    <span>
                      {selectedLocation.street_address}, {selectedLocation.postal_code} {selectedLocation.city}
                    </span>
                  </div>
                )}
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Datum *</label>
                  <input
                    type="date"
                    value={formData.date}
                    onChange={(e) => setFormData({ ...formData, date: e.target.value })}
                    min={new Date().toISOString().split('T')[0]}
                    required
                  />
                </div>

                <div className="form-group">
                  <label>Tid *</label>
                  <input
                    type="time"
                    value={formData.time}
                    onChange={(e) => setFormData({ ...formData, time: e.target.value })}
                    required
                  />
                </div>
              </div>

              <div className="form-group">
                <label>Anteckningar (valfritt)</label>
                <textarea
                  value={formData.notes}
                  onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
                  rows={4}
                  placeholder="Eventuella önskemål eller information..."
                />
              </div>

              <div className="booking-summary">
                <div className="summary-row">
                  <span>Behandling:</span>
                  <strong>{treatment.treatment_name}</strong>
                </div>
                <div className="summary-row">
                  <span>Längd:</span>
                  <strong>{treatment.time_duration} min</strong>
                </div>
                <div className="summary-row total">
                  <span>Totalt:</span>
                  <strong>{treatment.price} kr</strong>
                </div>
              </div>

              <button
                type="submit"
                className="btn btn-primary btn-submit"
                disabled={submitting}
              >
                {submitting ? 'Bokar...' : 'Bekräfta bokning'}
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}
