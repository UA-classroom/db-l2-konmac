import { useState, useRef, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Search, MapPin, Calendar, Heart, User, Settings, LogOut } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import './Header.css';

export default function Header() {
  const navigate = useNavigate();
  const { user } = useAuth();
  const [searchQuery, setSearchQuery] = useState('');
  const [location, setLocation] = useState('');
  const [showUserMenu, setShowUserMenu] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        setShowUserMenu(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleSearch = (e?: React.FormEvent) => {
    e?.preventDefault();
    const params = new URLSearchParams();
    if (searchQuery) params.set('q', searchQuery);
    if (location) params.set('location', location);
    navigate(`/treatments?${params.toString()}`);
  };

  return (
    <header className="header">
      <div className="header-top">
        <div className="container">
          <div className="header-content">
            <Link to="/" className="logo">
              <Calendar size={32} />
              <span>Bokadirekt</span>
            </Link>

            <form className="search-bar" onSubmit={handleSearch}>
              <Search className="search-icon" size={20} />
              <input
                type="text"
                placeholder="Vad vill du boka?"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
              <div className="location-input">
                <MapPin size={18} />
                <input
                  type="text"
                  placeholder="Var?"
                  value={location}
                  onChange={(e) => setLocation(e.target.value)}
                />
              </div>
              <button type="submit" className="search-button">
                <Search size={20} />
              </button>
            </form>

            <div className="header-actions">
              <Link to="/account/bookings" className="icon-button">
                <Calendar size={20} />
              </Link>
              <Link to="/favorites" className="icon-button">
                <Heart size={20} />
              </Link>
              <div className="user-menu-container" ref={menuRef}>
                <button
                  className="icon-button user-button"
                  onClick={() => setShowUserMenu(!showUserMenu)}
                >
                  <User size={20} />
                  {user && <span className="user-name">{user.first_name}</span>}
                </button>
                {showUserMenu && (
                  <div className="user-dropdown">
                    {user && (
                      <div className="user-info">
                        <div className="user-name-full">{user.first_name} {user.last_name}</div>
                        <div className="user-email">{user.email}</div>
                      </div>
                    )}
                    <div className="dropdown-divider"></div>
                    <Link to="/account" onClick={() => setShowUserMenu(false)}>
                      <User size={18} />
                      <span>Mitt konto</span>
                    </Link>
                    <Link to="/account/bookings" onClick={() => setShowUserMenu(false)}>
                      <Calendar size={18} />
                      <span>Mina bokningar</span>
                    </Link>
                    <Link to="/favorites" onClick={() => setShowUserMenu(false)}>
                      <Heart size={18} />
                      <span>Favoriter</span>
                    </Link>
                    <Link to="/account/settings" onClick={() => setShowUserMenu(false)}>
                      <Settings size={18} />
                      <span>Inställningar</span>
                    </Link>
                    <div className="dropdown-divider"></div>
                    <Link to="/login" onClick={() => setShowUserMenu(false)}>
                      <LogOut size={18} />
                      <span>Logga ut</span>
                    </Link>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>

      <nav className="header-nav">
        <div className="container">
          <ul className="nav-links">
            <li><Link to="/treatments">Alla behandlingar</Link></li>
            <li><Link to="/categories/1">Hår</Link></li>
            <li><Link to="/categories/4">Massage</Link></li>
            <li><Link to="/categories/2">Naglar</Link></li>
            <li><Link to="/categories/3">Ansiktsbehandling</Link></li>
            <li><Link to="/categories/5">Spa</Link></li>
            <li><Link to="/categories/6">Makeup</Link></li>
            <li><Link to="/categories/7">Vaxning</Link></li>
          </ul>
        </div>
      </nav>
    </header>
  );
}
