import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from './pages/Home';
import Treatments from './pages/Treatments';
import Users from './pages/Users';
import Customers from './pages/Customers';
import Businesses from './pages/Businesses';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app">
        <Navigation />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/treatments" element={<Treatments />} />
            <Route path="/users" element={<Users />} />
            <Route path="/customers" element={<Customers />} />
            <Route path="/businesses" element={<Businesses />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
