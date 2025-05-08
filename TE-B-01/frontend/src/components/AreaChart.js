import React from "react";
import { AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

function AreaChartComponent({ predictions }) {
  const data = Object.keys(predictions).map((model) => ({
    name: model,
    Humidity: predictions[model].humidity,
    Precipitation: predictions[model].precipitation,
  }));

  return (
    <ResponsiveContainer width="100%" height={300}>
      <AreaChart data={data}>
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Area type="monotone" dataKey="Humidity" stroke="#8884d8" fill="#8884d8" />
        <Area type="monotone" dataKey="Precipitation" stroke="#82ca9d" fill="#82ca9d" />
      </AreaChart>
    </ResponsiveContainer>
  );
}

export default AreaChartComponent;
