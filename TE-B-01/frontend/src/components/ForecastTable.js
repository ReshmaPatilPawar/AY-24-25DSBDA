import React from "react";

function ForecastTable({ predictions }) {
  return (
    <table className="forecast-table">
      <thead>
        <tr>
          <th>Model</th>
          <th>Max Temp (°C)</th>
          <th>Min Temp (°C)</th>
          <th>Wind Speed (km/h)</th>
          <th>Humidity (%)</th>
          <th>Precipitation (mm)</th>
        </tr>
      </thead>
      <tbody>
        {Object.keys(predictions).map((model) => (
          <tr key={model}>
            <td>{model}</td>
            <td>{predictions[model].max_temp}</td>
            <td>{predictions[model].min_temp}</td>
            <td>{predictions[model].wind_speed}</td>
            <td>{predictions[model].humidity}</td>
            <td>{predictions[model].precipitation}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default ForecastTable;
