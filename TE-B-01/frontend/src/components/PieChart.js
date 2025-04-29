import React from "react";
import { PieChart, Pie, Tooltip, ResponsiveContainer, Cell } from "recharts";

function PieChartComponent({ predictions }) {
  const COLORS = ["#0088FE", "#FFBB28", "#FF8042", "#FF4560"];

  const data = Object.keys(predictions).map((model, index) => ({
    name: model,
    Rainfall: predictions[model].precipitation,
    color: COLORS[index % COLORS.length],
  }));

  return (
    <ResponsiveContainer width="100%" height={300}>
      <PieChart>
        <Pie data={data} dataKey="Rainfall" nameKey="name" fill="#8884d8">
          {data.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={entry.color} />
          ))}
        </Pie>
        <Tooltip />
      </PieChart>
    </ResponsiveContainer>
  );
}

export default PieChartComponent;
