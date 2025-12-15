import { Calendar, Heart, User, LogOut } from 'lucide-react';
import './MyAccount.css';

export default function MyAccount() {
  return (
    <div className="my-account-page">
      <div className="container">
        <div className="account-header">
          <div className="user-avatar">
            <User size={48} />
          </div>
          <div className="user-info">
            <h1>Mitt konto</h1>
            <p>user@example.com</p>
          </div>
        </div>

        <div className="account-sections">
          <div className="account-card card">
            <div className="card-icon">
              <Calendar size={32} />
            </div>
            <h3>Mina bokningar</h3>
            <p>Hantera dina kommande och tidigare bokningar</p>
            <div className="empty-state-small">
              Inga bokningar ännu
            </div>
          </div>

          <div className="account-card card">
            <div className="card-icon">
              <Heart size={32} />
            </div>
            <h3>Mina favoriter</h3>
            <p>Dina sparade behandlingar och ställen</p>
            <div className="empty-state-small">
              Inga favoriter ännu
            </div>
          </div>

          <div className="account-card card">
            <div className="card-icon">
              <User size={32} />
            </div>
            <h3>Profilinställningar</h3>
            <p>Uppdatera dina personuppgifter</p>
            <button className="btn btn-secondary">
              Redigera profil
            </button>
          </div>
        </div>

        <button className="btn-logout">
          <LogOut size={20} />
          Logga ut
        </button>
      </div>
    </div>
  );
}
