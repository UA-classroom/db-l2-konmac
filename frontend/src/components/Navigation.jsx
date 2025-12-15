import { Link } from 'react-router-dom';

function Navigation() {
  return (
    <nav className="navbar">
      <div className="nav-brand">
        <Link to="/">Booking System</Link>
      </div>
      <ul className="nav-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/treatments">Treatments</Link></li>
        <li><Link to="/users">Users</Link></li>
        <li><Link to="/customers">Customers</Link></li>
        <li><Link to="/businesses">Businesses</Link></li>
      </ul>
    </nav>
  );
}

export default Navigation;