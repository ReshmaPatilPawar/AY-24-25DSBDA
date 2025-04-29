import React from "react";

function ExtremeWeatherAlert({ predictions }) {
  const alerts = [];

  Object.keys(predictions).forEach((model) => {
    const { max_temp, min_temp, wind_speed } = predictions[model];

    if (max_temp > 40) alerts.push(`🔥 High Temperature Alert from ${model}: ${max_temp}°C`);
    if (min_temp < 5) alerts.push(`❄️ Low Temperature Alert from ${model}: ${min_temp}°C`);
    if (wind_speed > 50) alerts.push(`💨 High Wind Speed Alert from ${model}: ${wind_speed} km/h`);
  });

  return (
    <div className="alert-box">
      {alerts.length > 0 ? alerts.map((alert, idx) => <p key={idx}>{alert}</p>) : <p>No extreme weather alerts</p>}
    </div>
  );
}

export default ExtremeWeatherAlert;
