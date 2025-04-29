import React from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

function LineChartComponent({ predictions }) {
  const data = Object.keys(predictions).map((model) => ({
    name: model,
    MaxTemp: predictions[model].max_temp,
    MinTemp: predictions[model].min_temp,
  }));

  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={data}>
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="MaxTemp" stroke="#FF5733" />
        <Line type="monotone" dataKey="MinTemp" stroke="#337AFF" />
      </LineChart>
    </ResponsiveContainer>
  );
}

export default LineChartComponent;
