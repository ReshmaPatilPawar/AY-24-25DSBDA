import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [inputs, setInputs] = useState({
    Temperature: '',
    Humidity: '',
    WindSpeed: '',
    GeneralDiffuseFlows: '',
    DiffuseFlows: '',
    Hour: '',
    Day: '',
    Month: ''
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setInputs({ ...inputs, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post('http://localhost:5000/predict', inputs);
    setResult(response.data);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Electricity Consumption Predictor</h2>
      <form onSubmit={handleSubmit}>
        {Object.keys(inputs).map(key => (
          <div key={key}>
            <label>{key}: </label>
            <input type="number" name={key} value={inputs[key]} onChange={handleChange} />
          </div>
        ))}
        <button type="submit">Predict</button>
      </form>

      {result && (
        <div>
          <h3>Predicted Consumption</h3>
          <p>Zone 1: {result.PowerConsumption_Zone1.toFixed(2)}</p>
          <p>Zone 2: {result.PowerConsumption_Zone2.toFixed(2)}</p>
          <p>Zone 3: {result.PowerConsumption_Zone3.toFixed(2)}</p>
        </div>
      )}
    </div>
  );
}

export default App;
