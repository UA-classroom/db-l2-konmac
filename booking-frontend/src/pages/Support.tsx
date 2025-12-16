import { useState } from 'react';
import { HelpCircle, MessageSquare, Phone, Mail, Send, CheckCircle } from 'lucide-react';
import './Support.css';

interface SupportTicket {
  id: string;
  subject: string;
  message: string;
  category: string;
  status: 'open' | 'in_progress' | 'resolved';
  created_at: string;
}

export default function Support() {
  const [showNewTicketForm, setShowNewTicketForm] = useState(false);
  const [tickets] = useState<SupportTicket[]>([
    {
      id: 'T-001',
      subject: 'Problem med bokning',
      message: 'Jag kan inte se min senaste bokning i min profil',
      category: 'Bokning',
      status: 'resolved',
      created_at: '2025-12-10',
    },
  ]);

  const [formData, setFormData] = useState({
    subject: '',
    category: 'Bokning',
    message: '',
  });

  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
    setTimeout(() => {
      setShowNewTicketForm(false);
      setSubmitted(false);
      setFormData({ subject: '', category: 'Bokning', message: '' });
    }, 2000);
  };

  const categories = [
    'Bokning',
    'Betalning',
    'Konto',
    'Tekniskt problem',
    'Annat',
  ];

  return (
    <div className="support-page">
      <div className="container">
        <div className="page-header">
          <h1>Support & Hjälp</h1>
          <p>Vi finns här för att hjälpa dig</p>
        </div>

        <div className="support-grid">
          <div className="support-main">
            <div className="support-section card">
              <div className="section-header">
                <h2>Kontakta oss</h2>
                <button
                  className="btn btn-primary"
                  onClick={() => setShowNewTicketForm(!showNewTicketForm)}
                >
                  <MessageSquare size={18} />
                  Nytt ärende
                </button>
              </div>

              {showNewTicketForm && (
                <div className="new-ticket-form">
                  {submitted ? (
                    <div className="success-message">
                      <CheckCircle size={48} />
                      <h3>Tack för ditt meddelande!</h3>
                      <p>Vi återkommer inom 24 timmar</p>
                    </div>
                  ) : (
                    <form onSubmit={handleSubmit}>
                      <div className="form-group">
                        <label htmlFor="category">Kategori</label>
                        <select
                          id="category"
                          value={formData.category}
                          onChange={(e) => setFormData({ ...formData, category: e.target.value })}
                          required
                        >
                          {categories.map(cat => (
                            <option key={cat} value={cat}>{cat}</option>
                          ))}
                        </select>
                      </div>

                      <div className="form-group">
                        <label htmlFor="subject">Ämne</label>
                        <input
                          type="text"
                          id="subject"
                          value={formData.subject}
                          onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
                          placeholder="Beskriv ditt problem kort"
                          required
                        />
                      </div>

                      <div className="form-group">
                        <label htmlFor="message">Meddelande</label>
                        <textarea
                          id="message"
                          value={formData.message}
                          onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                          placeholder="Beskriv ditt problem i detalj"
                          rows={6}
                          required
                        />
                      </div>

                      <div className="form-actions">
                        <button type="submit" className="btn btn-primary">
                          <Send size={18} />
                          Skicka ärende
                        </button>
                        <button
                          type="button"
                          className="btn btn-secondary"
                          onClick={() => setShowNewTicketForm(false)}
                        >
                          Avbryt
                        </button>
                      </div>
                    </form>
                  )}
                </div>
              )}
            </div>

            <div className="support-section card">
              <h2>Mina ärenden</h2>
              {tickets.length === 0 ? (
                <div className="empty-tickets">
                  <p>Du har inga öppna ärenden</p>
                </div>
              ) : (
                <div className="tickets-list">
                  {tickets.map(ticket => (
                    <div key={ticket.id} className="ticket-item">
                      <div className="ticket-header">
                        <div>
                          <h4>{ticket.subject}</h4>
                          <span className="ticket-id">Ärende {ticket.id}</span>
                        </div>
                        <span className={`ticket-status status-${ticket.status}`}>
                          {ticket.status === 'open' ? 'Öppet' :
                           ticket.status === 'in_progress' ? 'Pågående' : 'Löst'}
                        </span>
                      </div>
                      <div className="ticket-meta">
                        <span className="ticket-category">{ticket.category}</span>
                        <span className="ticket-date">{ticket.created_at}</span>
                      </div>
                      <p className="ticket-message">{ticket.message}</p>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          <div className="support-sidebar">
            <div className="contact-card card">
              <h3>Direktkontakt</h3>
              <div className="contact-methods">
                <div className="contact-method">
                  <Phone size={20} />
                  <div>
                    <strong>Telefon</strong>
                    <p>08-123 456 78</p>
                    <span className="hours">Mån-Fre 9-17</span>
                  </div>
                </div>
                <div className="contact-method">
                  <Mail size={20} />
                  <div>
                    <strong>Email</strong>
                    <p>support@bokadirekt.se</p>
                    <span className="hours">Svarar inom 24h</span>
                  </div>
                </div>
              </div>
            </div>

            <div className="faq-card card">
              <h3>Vanliga frågor</h3>
              <div className="faq-list">
                <div className="faq-item">
                  <HelpCircle size={18} />
                  <div>
                    <h4>Hur avbokar jag?</h4>
                    <p>Gå till Mina bokningar och klicka på Avboka</p>
                  </div>
                </div>
                <div className="faq-item">
                  <HelpCircle size={18} />
                  <div>
                    <h4>Kan jag ändra min bokning?</h4>
                    <p>Kontakta salongen direkt för att ändra din bokning</p>
                  </div>
                </div>
                <div className="faq-item">
                  <HelpCircle size={18} />
                  <div>
                    <h4>Hur betalar jag?</h4>
                    <p>Betalning sker på plats i salongen</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
