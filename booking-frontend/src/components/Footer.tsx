import { Link } from 'react-router-dom';
import './Footer.css';

export default function Footer() {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-column">
            <h4>Konto</h4>
            <ul>
              <li><Link to="/account/bookings">Mina bokningar</Link></li>
              <li><Link to="/favorites">Mina favoriter</Link></li>
              <li><Link to="/account">Använd presentkort</Link></li>
              <li><Link to="/account">Använd friskvårdskort</Link></li>
            </ul>
          </div>

          <div className="footer-column">
            <h4>Bokadirekt</h4>
            <ul>
              <li><Link to="/about">Om Bokadirekt</Link></li>
              <li><Link to="/blog">Blogg - Beautylabbet</Link></li>
              <li><Link to="/faq">FAQ - Skönhetsbehandlingar</Link></li>
              <li><Link to="/support">Support</Link></li>
            </ul>
          </div>

          <div className="footer-column">
            <h4>Villkor</h4>
            <ul>
              <li><Link to="/privacy">Etisk policy</Link></li>
              <li><Link to="/integrity">Integritetspolicy</Link></li>
              <li><Link to="/cookies">Cookies</Link></li>
              <li><Link to="/terms">Allmänna villkor</Link></li>
            </ul>
          </div>

          <div className="footer-column">
            <h4>För företag</h4>
            <ul>
              <li><Link to="/business">Bokadirekt för företag</Link></li>
              <li><Link to="/business/login">Företagsinloggning</Link></li>
            </ul>
          </div>
        </div>

        <div className="footer-bottom">
          <p>&copy; Bokadirekt {new Date().getFullYear()}</p>
          <div className="footer-social">
            <a href="#" aria-label="Instagram">Instagram</a>
            <a href="#" aria-label="Facebook">Facebook</a>
            <a href="#" aria-label="LinkedIn">LinkedIn</a>
          </div>
        </div>
      </div>
    </footer>
  );
}
