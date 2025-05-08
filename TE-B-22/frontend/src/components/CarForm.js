import React, { useState } from 'react';
import axios from 'axios';
import "./CarForm.css"
const makes = ["Acura", "Alfa Romeo", "Aston Martin", "Audi", "Bentley", "BMW", "Buick", "Cadillac", "Chevrolet", "Chrysler", "Dodge", "FIAT", "Ferrari", "Ford", "Genesis", "GMC", "Honda", "HUMMER", "Hyundai", "INFINITI", "Jaguar", "Jeep", "Kia", "Lamborghini", "Land Rover", "Lexus", "Lincoln", "Lotus", "Maserati", "Mazda", "McLaren", "Mercedes-Benz", "MINI", "Mitsubishi", "Nissan", "Porsche", "Ram", "Rolls-Royce", "Saab", "Scion", "smart", "Subaru", "Tesla", "Toyota", "Volkswagen", "Volvo"];
const bodies = ["Convertible", "Coupe", "Hatchback", "Pickup", "SUV", "Sedan", "Van", "Wagon"];
const transmissions = ["Automatic", "CVT", "Manual"];
const states = ["ak", "al", "ar", "az", "ca", "co", "ct", "dc", "de", "fl", "ga", "hi", "ia", "id", "il", "in", "ks", "ky", "la", "ma", "md", "me", "mi", "mn", "mo", "ms", "mt", "nc", "nd", "ne", "nh", "nj", "nm", "nv", "ny", "oh", "ok", "or", "pa", "ri", "sc", "sd", "tn", "tx", "ut", "va", "vt", "wa", "wi", "wv", "wy"];
const colors = ["Beige", "Black", "Blue", "Brown", "Burgundy", "Gold", "Gray", "Green", "Orange", "Purple", "Red", "Silver", "Turquoise", "White", "Yellow"];
const sellers = ["Private", "Dealer"];

const CarForm = () => {
  const [formData, setFormData] = useState({
    year: '',
    make: '',
    model: '',
    trim: '',
    body: '',
    transmission: '',
    state: '',
    condition: '',
    odometer: '',
    color: '',
    interior: '',
    seller: '',
    mmr: ''
  });

  const [predictedPrice, setPredictedPrice] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setPredictedPrice(null);
    setLoading(true);

    try {
      const cleanedData = {
        ...formData,
        year: parseInt(formData.year),
        odometer: parseFloat(formData.odometer),
        condition: parseFloat(formData.condition),
        mmr: parseFloat(formData.mmr)
      };

      const response = await axios.post('http://localhost:5000/predict', cleanedData);
      setPredictedPrice(response.data.predicted_price);
    } catch (err) {
      setError(err.response?.data?.error || 'Prediction failed.');
    }

    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: '0 auto' }}>
      <h2>Car Price Predictor</h2>
      <form onSubmit={handleSubmit}>
        {/* Year */}
        <div>
          <label htmlFor="year">Year:</label>
          <input type="number" name="year" id="year" value={formData.year} onChange={handleChange} required />
        </div>

        {/* Make */}
        <div>
          <label htmlFor="make">Make:</label>
          <select name="make" id="make" value={formData.make} onChange={handleChange} required>
            <option value="">Select Make</option>
            {makes.map(make => <option key={make} value={make}>{make}</option>)}
          </select>
        </div>

        {/* Model */}
        <div>
          <label htmlFor="model">Model:</label>
          <input type="text" name="model" id="model" value={formData.model} onChange={handleChange} required />
        </div>

        {/* Trim */}
        <div>
          <label htmlFor="trim">Trim:</label>
          <input type="text" name="trim" id="trim" value={formData.trim} onChange={handleChange} />
        </div>

        {/* Body */}
        <div>
          <label htmlFor="body">Body:</label>
          <select name="body" id="body" value={formData.body} onChange={handleChange} required>
            <option value="">Select Body</option>
            {bodies.map(body => <option key={body} value={body}>{body}</option>)}
          </select>
        </div>

        {/* Transmission */}
        <div>
          <label htmlFor="transmission">Transmission:</label>
          <select name="transmission" id="transmission" value={formData.transmission} onChange={handleChange} required>
            <option value="">Select Transmission</option>
            {transmissions.map(t => <option key={t} value={t}>{t}</option>)}
          </select>
        </div>

        {/* State */}
        <div>
          <label htmlFor="state">State:</label>
          <select name="state" id="state" value={formData.state} onChange={handleChange} required>
            <option value="">Select State</option>
            {states.map(s => <option key={s} value={s}>{s.toUpperCase()}</option>)}
          </select>
        </div>

        {/* Condition */}
        <div>
          <label htmlFor="condition">Condition (0-5):</label>
          <input type="number" step="0.1" name="condition" id="condition" value={formData.condition} onChange={handleChange} required />
        </div>

        {/* Odometer */}
        <div>
          <label htmlFor="odometer">Odometer:</label>
          <input type="number" name="odometer" id="odometer" value={formData.odometer} onChange={handleChange} required />
        </div>

        {/* Color */}
        <div>
          <label htmlFor="color">Color:</label>
          <select name="color" id="color" value={formData.color} onChange={handleChange} required>
            <option value="">Select Color</option>
            {colors.map(color => <option key={color} value={color}>{color}</option>)}
          </select>
        </div>

        {/* Interior */}
        {/* Interior */}
        <div>
          <label htmlFor="interior">Interior Color:</label>
          <select name="interior" id="interior" value={formData.interior} onChange={handleChange} required>
            <option value="">Select Interior</option>
            {colors.map(int => <option key={int} value={int}>{int}</option>)}
          </select>
        </div>

        {/* Seller */}
        <div>
          <label htmlFor="seller">Seller:</label>
          <select name="seller" id="seller" value={formData.seller} onChange={handleChange} required>
            <option value="">Select Seller</option>
            {sellers.map(s => <option key={s} value={s}>{s}</option>)}
          </select>
        </div>

        {/* MMR */}
        <div>
          <label htmlFor="mmr">MMR:</label>
          <input type="number" name="mmr" id="mmr" value={formData.mmr} onChange={handleChange} required />
        </div>

        <div style={{ marginTop: 20 }}>
          <button type="submit" disabled={loading}>
            {loading ? 'Predicting...' : 'Predict Price'}
          </button>
        </div>
      </form>

      {predictedPrice !== null && (
        <div style={{ marginTop: 20 }}>
          <h3>Predicted Selling Price: <span style={{ color: 'green' }}>${predictedPrice}</span></h3>
        </div>
      )}

      {error && (
        <div style={{ marginTop: 20 }}>
          <p style={{ color: 'red' }}>{error}</p>
        </div>
      )}
    </div>
  );
};

export default CarForm;
