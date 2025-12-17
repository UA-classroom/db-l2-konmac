import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { getTreatments, getTreatmentCategories } from '../services/api';
import type { Treatment, TreatmentCategory } from '../types';
import { Heart, Clock, DollarSign } from 'lucide-react';
import { getTreatmentPrice, formatPrice } from '../utils/pricing';
import './MyFavorites.css';

export default function MyFavorites() {
  const [favorites, setFavorites] = useState<number[]>([]);
  const [treatments, setTreatments] = useState<Treatment[]>([]);
  const [categories, setCategories] = useState<TreatmentCategory[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Load favorites from localStorage
    const storedFavorites = localStorage.getItem('favorites');
    if (storedFavorites) {
      setFavorites(JSON.parse(storedFavorites));
    }
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [treatmentsRes, categoriesRes] = await Promise.all([
        getTreatments(),
        getTreatmentCategories(),
      ]);

      const treatmentsData = treatmentsRes.data.treatments || treatmentsRes.data || [];
      const categoriesData = categoriesRes.data.treatment_categories || categoriesRes.data || [];

      setTreatments(Array.isArray(treatmentsData) ? treatmentsData : []);
      setCategories(Array.isArray(categoriesData) ? categoriesData : []);
      setError(null);
    } catch (err: any) {
      console.error('Error fetching data:', err);
      setError(err.response?.data?.detail || err.message || 'Failed to fetch data');
    } finally {
      setLoading(false);
    }
  };

  const removeFavorite = (treatmentId: number) => {
    const newFavorites = favorites.filter(id => id !== treatmentId);
    setFavorites(newFavorites);
    localStorage.setItem('favorites', JSON.stringify(newFavorites));
  };

  const favoriteTreatments = treatments.filter(t => favorites.includes(t.treatment_id));

  return (
    <div className="my-favorites-page">
      <div className="container">
        <div className="page-header">
          <h1>Mina favoriter</h1>
          <p>Dina sparade behandlingar</p>
        </div>

        {loading && <div className="loading">Laddar favoriter...</div>}
        {error && <div className="error">{error}</div>}

        {!loading && !error && favoriteTreatments.length === 0 && (
          <div className="empty-state">
            <Heart size={48} />
            <h3>Inga favoriter ännu</h3>
            <p>Spara behandlingar du gillar genom att klicka på hjärtat</p>
            <Link to="/treatments" className="btn btn-primary">
              Bläddra behandlingar
            </Link>
          </div>
        )}

        {!loading && !error && favoriteTreatments.length > 0 && (
          <div className="favorites-grid">
            {favoriteTreatments.map((treatment) => {
              const category = categories.find(
                (c) => c.category_id === treatment.category_id
              );

              return (
                <div key={treatment.treatment_id} className="favorite-card card">
                  <div className="treatment-image">
                    <img
                      src={treatment.image_url || 'https://images.unsplash.com/photo-1519415387722-a1c3bbef716c?w=400'}
                      alt={treatment.treatment_name}
                    />
                    {category && (
                      <span className="treatment-category-badge">
                        {category.category_name}
                      </span>
                    )}
                    <button
                      className="favorite-button active"
                      onClick={() => removeFavorite(treatment.treatment_id)}
                    >
                      <Heart size={20} fill="currentColor" />
                    </button>
                  </div>
                  <div className="treatment-content">
                    <h3>{treatment.treatment_name}</h3>
                    {treatment.treatment_description && (
                      <p className="treatment-description">{treatment.treatment_description}</p>
                    )}
                    <div className="treatment-meta">
                      <span className="treatment-duration">
                        <Clock size={16} />
                        {treatment.time_duration} min
                      </span>
                      <span className="treatment-price">
                        <DollarSign size={16} />
                        {formatPrice(getTreatmentPrice(treatment.category_id, treatment.time_duration))}
                      </span>
                    </div>
                    <Link
                      to={`/treatment/${treatment.treatment_id}`}
                      className="btn btn-primary btn-book"
                    >
                      Boka nu
                    </Link>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
