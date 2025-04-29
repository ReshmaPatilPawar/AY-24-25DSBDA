import React, { useState } from "react";
import axios from "axios";
import ForecastTable from "./components/ForecastTable";
import ExtremeWeatherAlert from "./components/ExtremeWeatherAlert";
import BarChart from "./components/BarChart";
import LineChart from "./components/LineChart";
import AreaChart from "./components/AreaChart";
import PieChart from "./components/PieChart";
import RadarChart from "./components/RadarChart";
import "./App.css";

function App() {
  const [date, setDate] = useState("");
  const [predictions, setPredictions] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    setDate(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!date) return;
    
    setIsLoading(true);
    const [year, month, day] = date.split("-");
    try {
      const res = await axios.post("http://127.0.0.1:5000/predict", { year, month, day });
      setPredictions(res.data);
    } catch (err) {
      console.error("Error fetching predictions:", err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <nav className="navbar">
        <div className="navbar-content">
          <h1>Weather Prediction Dashboard</h1>
          <div className="nav-links">
            <span>Home</span>
            <span>Analytics</span>
            <span>Historical Data</span>
          </div>
        </div>
      </nav>

      <div className="main-content">
        <main className="dashboard">
          <section className="hero">
            <h2>Weather Forecasting Analytics</h2>
            <p>Select a date to view detailed weather predictions and trends</p>
          </section>

          <form onSubmit={handleSubmit} className="form">
            <div className="input-group">
              <label htmlFor="date-input">Select Date:</label>
              <input 
                id="date-input"
                type="date" 
                value={date} 
                onChange={handleChange} 
                required 
                className="input" 
              />
            </div>
            <button type="submit" className="button" disabled={isLoading}>
              {isLoading ? (
                <>
                  <span className="spinner"></span> Processing...
                </>
              ) : (
                "Generate Report"
              )}
            </button>
          </form>

          {predictions && (
            <div className="results-container">
              <ExtremeWeatherAlert predictions={predictions} />
              <ForecastTable predictions={predictions} />
              
              <section className="chart-section">
                <h3 className="section-title">Temperature Metrics</h3>
                <div className="chart-row">
                  <BarChart predictions={predictions} />
                  <LineChart predictions={predictions} />
                </div>
              </section>

              <section className="chart-section">
                <h3 className="section-title">Atmospheric Conditions</h3>
                <div className="chart-row">
                  <AreaChart predictions={predictions} />
                  <PieChart predictions={predictions} />
                </div>
              </section>

              <section className="chart-section">
                <h3 className="section-title">Wind Analysis</h3>
                <div className="chart-row">
                  <RadarChart predictions={predictions} />
                </div>
              </section>
            </div>
          )}
        </main>
      </div>

      <footer className="footer">
        <p>© {new Date().getFullYear()} Weather Analytics Platform. All data is predictive.</p>
      </footer>
    </div>
  );
}

export default App;