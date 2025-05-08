import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";

function BarChartComponent({ predictions }) {
  const data = Object.keys(predictions).map((model) => ({
    name: model,
    MaxTemp: predictions[model].max_temp,
    MinTemp: predictions[model].min_temp,
  }));

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data}>
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="MaxTemp" fill="#FF5733" />
        <Bar dataKey="MinTemp" fill="#337AFF" />
      </BarChart>
    </ResponsiveContainer>
  );
}

export default BarChartComponent;
