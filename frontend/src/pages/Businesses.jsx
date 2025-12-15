import { useState, useEffect } from 'react';
import { getBusinesses, createBusiness, updateBusiness } from '../services/api';

function Businesses() {
  const [businesses, setBusinesses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [editingBusiness, setEditingBusiness] = useState(null);

  const [formData, setFormData] = useState({
    business_name: '',
    email: '',
    phone_number: '',
    about_text: ''
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const response = await getBusinesses();
      console.log('Businesses response:', response.data);

      const businessesData = response.data.businesses || response.data || [];
      setBusinesses(Array.isArray(businessesData) ? businessesData : []);
      setError(null);
    } catch (err) {
      console.error('Error fetching businesses:', err);
      setError(err.response?.data?.detail || err.message || 'Failed to fetch businesses');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingBusiness) {
        await updateBusiness(editingBusiness.business_id, formData);
      } else {
        await createBusiness(formData);
      }
      resetForm();
      fetchData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to save business');
    }
  };

  const handleEdit = (business) => {
    setEditingBusiness(business);
    setFormData({
      business_name: business.business_name,
      email: business.email,
      phone_number: business.phone_number,
      about_text: business.about_text
    });
    setIsFormVisible(true);
  };

  const resetForm = () => {
    setFormData({
      business_name: '',
      email: '',
      phone_number: '',
      about_text: ''
    });
    setEditingBusiness(null);
    setIsFormVisible(false);
  };

  if (loading) return <div className="loading">Loading...</div>;

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>Businesses</h1>
        <button onClick={() => setIsFormVisible(!isFormVisible)} className="btn-primary">
          {isFormVisible ? 'Cancel' : 'Add Business'}
        </button>
      </div>

      {error && <div className="error-message">{error}</div>}

      {isFormVisible && (
        <div className="form-container">
          <h2>{editingBusiness ? 'Edit Business' : 'New Business'}</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Business Name:</label>
              <input
                type="text"
                value={formData.business_name}
                onChange={(e) => setFormData({ ...formData, business_name: e.target.value })}
                required
              />
            </div>
            <div className="form-group">
              <label>Email:</label>
              <input
                type="email"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                required
              />
            </div>
            <div className="form-group">
              <label>Phone Number:</label>
              <input
                type="tel"
                value={formData.phone_number}
                onChange={(e) => setFormData({ ...formData, phone_number: e.target.value })}
              />
            </div>
            <div className="form-group">
              <label>About:</label>
              <textarea
                value={formData.about_text}
                onChange={(e) => setFormData({ ...formData, about_text: e.target.value })}
                rows="4"
              />
            </div>
            <div className="form-actions">
              <button type="submit" className="btn-primary">
                {editingBusiness ? 'Update' : 'Create'}
              </button>
              <button type="button" onClick={resetForm} className="btn-secondary">
                Cancel
              </button>
            </div>
          </form>
        </div>
      )}

      <div className="table-container">
        {businesses.length === 0 ? (
          <div className="empty-state">No businesses found. Create one to get started!</div>
        ) : (
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Business Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>About</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {businesses.map((business) => (
                <tr key={business.business_id}>
                  <td>{business.business_id}</td>
                  <td>{business.business_name}</td>
                  <td>{business.email}</td>
                  <td>{business.phone_number}</td>
                  <td>{business.about_text}</td>
                  <td className="action-buttons">
                    <button onClick={() => handleEdit(business)} className="btn-edit">
                      Edit
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}

export default Businesses;