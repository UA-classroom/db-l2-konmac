import { useState, useEffect } from 'react';
import { getCustomers, getUsers, createCustomer, updateCustomer, deleteCustomer } from '../services/api';

function Customers() {
  const [customers, setCustomers] = useState([]);
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [editingCustomer, setEditingCustomer] = useState(null);

  const [formData, setFormData] = useState({
    user_id: '',
    balance: 0
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [customersRes, usersRes] = await Promise.all([
        getCustomers(),
        getUsers()
      ]);
      console.log('Customers response:', customersRes.data);
      console.log('Users for customers:', usersRes.data);

      const customersData = customersRes.data.customers || customersRes.data || [];
      const usersData = usersRes.data.customers || usersRes.data.users || usersRes.data || [];

      setCustomers(Array.isArray(customersData) ? customersData : []);
      setUsers(Array.isArray(usersData) ? usersData : []);
      setError(null);
    } catch (err) {
      console.error('Error fetching data:', err);
      setError(err.response?.data?.detail || err.message || 'Failed to fetch data');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingCustomer) {
        await updateCustomer(editingCustomer.customer_id, formData);
      } else {
        await createCustomer(formData);
      }
      resetForm();
      fetchData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to save customer');
    }
  };

  const handleEdit = (customer) => {
    setEditingCustomer(customer);
    setFormData({
      user_id: customer.user_id,
      balance: customer.balance
    });
    setIsFormVisible(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this customer?')) return;
    try {
      await deleteCustomer(id);
      fetchData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to delete customer');
    }
  };

  const resetForm = () => {
    setFormData({
      user_id: '',
      balance: 0
    });
    setEditingCustomer(null);
    setIsFormVisible(false);
  };

  const getUserName = (userId) => {
    const user = users.find(u => u.user_id === userId);
    return user ? `${user.first_name} ${user.last_name}` : 'Unknown';
  };

  if (loading) return <div className="loading">Loading...</div>;

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>Customers</h1>
        <button onClick={() => setIsFormVisible(!isFormVisible)} className="btn-primary">
          {isFormVisible ? 'Cancel' : 'Add Customer'}
        </button>
      </div>

      {error && <div className="error-message">{error}</div>}

      {isFormVisible && (
        <div className="form-container">
          <h2>{editingCustomer ? 'Edit Customer' : 'New Customer'}</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>User:</label>
              <select
                value={formData.user_id}
                onChange={(e) => setFormData({ ...formData, user_id: e.target.value })}
                required
              >
                <option value="">Select a user</option>
                {users.map((user) => (
                  <option key={user.user_id} value={user.user_id}>
                    {user.first_name} {user.last_name} ({user.email})
                  </option>
                ))}
              </select>
            </div>
            <div className="form-group">
              <label>Balance:</label>
              <input
                type="number"
                step="0.01"
                value={formData.balance}
                onChange={(e) => setFormData({ ...formData, balance: e.target.value })}
                required
              />
            </div>
            <div className="form-actions">
              <button type="submit" className="btn-primary">
                {editingCustomer ? 'Update' : 'Create'}
              </button>
              <button type="button" onClick={resetForm} className="btn-secondary">
                Cancel
              </button>
            </div>
          </form>
        </div>
      )}

      <div className="table-container">
        {customers.length === 0 ? (
          <div className="empty-state">No customers found. Create one to get started!</div>
        ) : (
          <table>
            <thead>
              <tr>
                <th>Customer ID</th>
                <th>User ID</th>
                <th>User Name</th>
                <th>Balance</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {customers.map((customer) => (
                <tr key={customer.customer_id}>
                  <td>{customer.customer_id}</td>
                  <td>{customer.user_id}</td>
                  <td>{getUserName(customer.user_id)}</td>
                  <td>${parseFloat(customer.balance).toFixed(2)}</td>
                  <td className="action-buttons">
                    <button onClick={() => handleEdit(customer)} className="btn-edit">
                      Edit
                    </button>
                    <button onClick={() => handleDelete(customer.customer_id)} className="btn-delete">
                      Delete
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

export default Customers;