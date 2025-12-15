import { useState, useEffect } from 'react';
import { getTreatments, getTreatmentCategories, createTreatment, updateTreatment, deleteTreatment } from '../services/api';

function Treatments() {
  const [treatments, setTreatments] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [editingTreatment, setEditingTreatment] = useState(null);

  const [formData, setFormData] = useState({
    treatment_name: '',
    treatment_description: '',
    category_id: '',
    time_duration: '',
    last_min_deal: false
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [treatmentsRes, categoriesRes] = await Promise.all([
        getTreatments(),
        getTreatmentCategories()
      ]);
      console.log('Treatments response:', treatmentsRes.data);
      console.log('Categories response:', categoriesRes.data);

      const treatmentsData = treatmentsRes.data.treatments || treatmentsRes.data || [];
      const categoriesData = categoriesRes.data.treatment_categories || categoriesRes.data || [];

      setTreatments(Array.isArray(treatmentsData) ? treatmentsData : []);
      setCategories(Array.isArray(categoriesData) ? categoriesData : []);
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
      if (editingTreatment) {
        await updateTreatment(editingTreatment.treatment_id, formData);
      } else {
        await createTreatment(formData);
      }
      resetForm();
      fetchData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to save treatment');
    }
  };

  const handleEdit = (treatment) => {
    setEditingTreatment(treatment);
    setFormData({
      treatment_name: treatment.treatment_name,
      treatment_description: treatment.treatment_description,
      category_id: treatment.category_id,
      time_duration: treatment.time_duration,
      last_min_deal: treatment.last_min_deal
    });
    setIsFormVisible(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this treatment?')) return;
    try {
      await deleteTreatment(id);
      fetchData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to delete treatment');
    }
  };

  const resetForm = () => {
    setFormData({
      treatment_name: '',
      treatment_description: '',
      category_id: '',
      time_duration: '',
      last_min_deal: false
    });
    setEditingTreatment(null);
    setIsFormVisible(false);
  };

  if (loading) return <div className="loading">Loading...</div>;

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>Treatments</h1>
        <button onClick={() => setIsFormVisible(!isFormVisible)} className="btn-primary">
          {isFormVisible ? 'Cancel' : 'Add Treatment'}
        </button>
      </div>

      {error && <div className="error-message">{error}</div>}

      {isFormVisible && (
        <div className="form-container">
          <h2>{editingTreatment ? 'Edit Treatment' : 'New Treatment'}</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Treatment Name:</label>
              <input
                type="text"
                value={formData.treatment_name}
                onChange={(e) => setFormData({ ...formData, treatment_name: e.target.value })}
                required
              />
            </div>
            <div className="form-group">
              <label>Description:</label>
              <textarea
                value={formData.treatment_description}
                onChange={(e) => setFormData({ ...formData, treatment_description: e.target.value })}
              />
            </div>
            <div className="form-group">
              <label>Category:</label>
              <select
                value={formData.category_id}
                onChange={(e) => setFormData({ ...formData, category_id: e.target.value })}
                required
              >
                <option value="">Select a category</option>
                {categories.map((cat) => (
                  <option key={cat.category_id} value={cat.category_id}>
                    {cat.category_name}
                  </option>
                ))}
              </select>
            </div>
            <div className="form-group">
              <label>Duration (minutes):</label>
              <input
                type="number"
                value={formData.time_duration}
                onChange={(e) => setFormData({ ...formData, time_duration: e.target.value })}
                required
              />
            </div>
            <div className="form-group">
              <label>
                <input
                  type="checkbox"
                  checked={formData.last_min_deal}
                  onChange={(e) => setFormData({ ...formData, last_min_deal: e.target.checked })}
                />
                Last Minute Deal
              </label>
            </div>
            <div className="form-actions">
              <button type="submit" className="btn-primary">
                {editingTreatment ? 'Update' : 'Create'}
              </button>
              <button type="button" onClick={resetForm} className="btn-secondary">
                Cancel
              </button>
            </div>
          </form>
        </div>
      )}

      <div className="table-container">
        {treatments.length === 0 ? (
          <div className="empty-state">No treatments found. Create one to get started!</div>
        ) : (
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Description</th>
                <th>Duration (min)</th>
                <th>Last Min Deal</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {treatments.map((treatment) => (
                <tr key={treatment.treatment_id}>
                  <td>{treatment.treatment_id}</td>
                  <td>{treatment.treatment_name}</td>
                  <td>{treatment.treatment_description}</td>
                  <td>{treatment.time_duration}</td>
                  <td>{treatment.last_min_deal ? 'Yes' : 'No'}</td>
                  <td className="action-buttons">
                    <button onClick={() => handleEdit(treatment)} className="btn-edit">
                      Edit
                    </button>
                    <button onClick={() => handleDelete(treatment.treatment_id)} className="btn-delete">
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

export default Treatments;