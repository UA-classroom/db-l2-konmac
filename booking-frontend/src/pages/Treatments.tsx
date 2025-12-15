import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getTreatments, getTreatmentCategories } from '../services/api';
import type { Treatment, TreatmentCategory } from '../types';
import { Clock, DollarSign, Search } from 'lucide-react';
import './Treatments.css';

export default function Treatments() {
  const { categoryId } = useParams();
  const [treatments, setTreatments] = useState<Treatment[]>([]);
  const [categories, setCategories] = useState<TreatmentCategory[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<number | null>(
    categoryId ? parseInt(categoryId) : null
  );

  useEffect(() => {
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

  const filteredTreatments = treatments.filter((treatment) => {
    const matchesSearch = treatment.treatment_name
      .toLowerCase()
      .includes(searchQuery.toLowerCase()) ||
      treatment.treatment_description?.toLowerCase().includes(searchQuery.toLowerCase());

    const matchesCategory = selectedCategory === null ||
      treatment.category_id === selectedCategory;

    return matchesSearch && matchesCategory;
  });

  return (
    <div className="treatments-page">
      <div className="container">
        <div className="treatments-header">
          <h1>Boka behandling</h1>
          <p>Hitta och boka den perfekta behandlingen för dig</p>
        </div>

        <div className="search-filter-section">
          <div className="search-box">
            <Search size={20} />
            <input
              type="text"
              placeholder="Sök behandlingar..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>

          <div className="category-filters">
            <button
              className={`filter-btn ${selectedCategory === null ? 'active' : ''}`}
              onClick={() => setSelectedCategory(null)}
            >
              Alla
            </button>
            {categories.map((category) => (
              <button
                key={category.category_id}
                className={`filter-btn ${selectedCategory === category.category_id ? 'active' : ''}`}
                onClick={() => setSelectedCategory(category.category_id)}
              >
                {category.category_name}
              </button>
            ))}
          </div>
        </div>

        {loading && <div className="loading">Laddar behandlingar...</div>}
        {error && <div className="error">{error}</div>}

        {!loading && !error && filteredTreatments.length === 0 && (
          <div className="empty-state">
            {searchQuery || selectedCategory !== null
              ? 'Inga behandlingar matchade din sökning'
              : 'Inga behandlingar hittades'}
          </div>
        )}

        {!loading && !error && filteredTreatments.length > 0 && (
          <div className="treatments-grid">
            {filteredTreatments.map((treatment) => {
              const category = categories.find(
                (c) => c.category_id === treatment.category_id
              );

              return (
                <Link
                  key={treatment.treatment_id}
                  to={`/treatment/${treatment.treatment_id}`}
                  className="treatment-card card"
                >
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
                        {treatment.price} kr
                      </span>
                    </div>
                    <button className="btn btn-primary btn-book">
                      Boka nu
                    </button>
                  </div>
                </Link>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
