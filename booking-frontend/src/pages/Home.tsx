import { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { getTreatmentCategories } from '../services/api';
import type { TreatmentCategory } from '../types';
import { Search } from 'lucide-react';
import './Home.css';

export default function Home() {
  const navigate = useNavigate();
  const [categories, setCategories] = useState<TreatmentCategory[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [location, setLocation] = useState('');

  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = async () => {
    try {
      setLoading(true);
      const response = await getTreatmentCategories();
      const categoriesData = response.data.treatment_categories || response.data || [];
      setCategories(Array.isArray(categoriesData) ? categoriesData : []);
      setError(null);
    } catch (err: any) {
      console.error('Error fetching categories:', err);
      setError(err.response?.data?.detail || err.message || 'Failed to fetch categories');
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = (e?: React.FormEvent) => {
    e?.preventDefault();
    const params = new URLSearchParams();
    if (searchQuery) params.set('q', searchQuery);
    if (location) params.set('location', location);
    navigate(`/treatments?${params.toString()}`);
  };

  // Category images mapping
  const categoryImages: Record<string, string> = {
    'Hår': 'https://images.unsplash.com/photo-1560066984-138dadb4c035?w=400',
    'Massage': 'https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=400',
    'Naglar': 'https://images.unsplash.com/photo-1604654894610-df63bc536371?w=400',
    'Ansiktsbehandling': 'https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=400',
    'Spa': 'https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=400',
    'Makeup': 'https://images.unsplash.com/photo-1487412912498-0447578fcca8?w=400',
    'Vaxning': 'https://images.unsplash.com/photo-1519415387722-a1c3bbef716c?w=400',
    'Skönhet': 'https://images.unsplash.com/photo-1487412912498-0447578fcca8?w=400',
  };

  return (
    <div className="home">
      <section className="hero">
        <div className="hero-content">
          <h1>Allt inom skönhet och hälsa</h1>
          <form className="hero-search" onSubmit={handleSearch}>
            <Search className="search-icon" size={24} />
            <input
              type="text"
              placeholder="Vad vill du boka?"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
            <input
              type="text"
              placeholder="Var?"
              value={location}
              onChange={(e) => setLocation(e.target.value)}
            />
            <button type="submit" className="btn btn-primary">
              Sök
            </button>
          </form>
        </div>
      </section>

      <section className="categories-section">
        <div className="container">
          <h2>Kategorier</h2>

          {loading && <div className="loading">Laddar kategorier...</div>}
          {error && <div className="error">{error}</div>}

          {!loading && !error && categories.length === 0 && (
            <div className="empty-state">Inga kategorier hittades</div>
          )}

          {!loading && !error && categories.length > 0 && (
            <div className="categories-grid">
              {categories.map((category) => (
                <Link
                  key={category.category_id}
                  to={`/categories/${category.category_id}`}
                  className="category-card card"
                >
                  <div className="category-image">
                    <img
                      src={category.image_url || categoryImages[category.category_name] || 'https://images.unsplash.com/photo-1519415387722-a1c3bbef716c?w=400'}
                      alt={category.category_name}
                    />
                  </div>
                  <div className="category-info">
                    <h3>{category.category_name}</h3>
                    {category.description && <p>{category.description}</p>}
                  </div>
                </Link>
              ))}
            </div>
          )}
        </div>
      </section>
    </div>
  );
}
