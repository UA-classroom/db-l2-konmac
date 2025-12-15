function Home() {
  return (
    <div className="page-container">
      <h1>Booking Management System</h1>
      <div className="home-content">
        <p>Welcome to the Booking Management System. Use the navigation menu to:</p>
        <ul>
          <li>Manage treatments and treatment categories</li>
          <li>View and edit users and customers</li>
          <li>Manage businesses and business locations</li>
          <li>Handle employees and owners</li>
          <li>Create and track bookings</li>
        </ul>
        <div className="info-card">
          <h2>Getting Started</h2>
          <p>Make sure your FastAPI backend is running on port 8000.</p>
          <p>Start by creating some treatment categories and treatments, then add users and customers.</p>
        </div>
      </div>
    </div>
  );
}

export default Home;