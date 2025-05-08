import React from 'react';

interface ResultChartProps {
  data: any;
  yieldValue: number;
}

const ResultChart: React.FC<ResultChartProps> = ({ data, yieldValue }) => {
  // This is a simplified chart component
  // In a real app, you would use a library like Chart.js, Recharts, etc.
  
  const factors = [
    { name: 'Temperature', value: data.temperature, max: 50, color: 'bg-red-400' },
    { name: 'Humidity', value: data.humidity, max: 100, color: 'bg-blue-400' },
    { name: 'Rainfall', value: Math.min(data.rainfall / 10, 100), max: 100, color: 'bg-blue-500' },
    { name: 'Nitrogen', value: data.nitrogen, max: 100, color: 'bg-green-500' },
    { name: 'Phosphorus', value: data.phosphorus, max: 100, color: 'bg-yellow-500' },
    { name: 'Potassium', value: data.potassium, max: 100, color: 'bg-purple-500' },
    { name: 'pH Level', value: (data.ph / 14) * 100, max: 100, color: 'bg-orange-400' },
  ];

  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow">
      <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">Factor Analysis</h3>
      
      <div className="space-y-4">
        {factors.map((factor) => (
          <div key={factor.name} className="relative">
            <div className="flex justify-between mb-1">
              <span className="text-sm font-medium text-gray-700 dark:text-gray-300">{factor.name}</span>
              <span className="text-sm font-medium text-gray-700 dark:text-gray-300">
                {factor.name === 'pH Level' ? data.ph : factor.value}
                {factor.name === 'Temperature' ? '°C' : factor.name === 'Humidity' ? '%' : factor.name === 'Rainfall' ? 'mm' : ''}
              </span>
            </div>
            <div className="w-full bg-gray-200 dark:bg-gray-600 rounded-full h-2.5">
              <div 
                className={`${factor.color} h-2.5 rounded-full transition-all duration-1000 ease-out`}
                style={{ width: `${(factor.value / factor.max) * 100}%` }}
              ></div>
            </div>
          </div>
        ))}
      </div>
      
      <div className="mt-6 pt-6 border-t border-gray-200 dark:border-gray-700">
        <h4 className="text-md font-medium text-gray-800 dark:text-white mb-3">Estimated Yield Comparison</h4>
        <div className="relative pt-1">
          <div className="flex items-center justify-between">
            <div>
              <span className="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-green-600 bg-green-200 dark:bg-green-900 dark:text-green-300">
                Your Expected Yield
              </span>
            </div>
            <div className="text-right">
              <span className="text-xs font-semibold inline-block text-green-600 dark:text-green-400">
                {yieldValue} tons/hectare
              </span>
            </div>
          </div>
          <div className="flex h-2 mt-2 overflow-hidden text-xs bg-green-200 dark:bg-green-900 rounded">
            <div
              style={{ width: `${Math.min((yieldValue / 15) * 100, 100)}%` }}
              className="flex flex-col justify-center text-center text-white bg-green-600 shadow-none whitespace-nowrap transition-all duration-1000 ease-out"
            ></div>
          </div>
          <div className="flex items-center justify-between mt-2">
            <div>
              <span className="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-gray-200 dark:bg-gray-700 dark:text-gray-300">
                Average Yield for {data.cropType}
              </span>
            </div>
            <div className="text-right">
              <span className="text-xs font-semibold inline-block text-gray-600 dark:text-gray-400">
                {(yieldValue * 0.8).toFixed(2)} tons/hectare
              </span>
            </div>
          </div>
          <div className="flex h-2 mt-2 overflow-hidden text-xs bg-gray-200 dark:bg-gray-700 rounded">
            <div
              style={{ width: `${Math.min(((yieldValue * 0.8) / 15) * 100, 100)}%` }}
              className="flex flex-col justify-center text-center text-white bg-gray-500 shadow-none whitespace-nowrap transition-all duration-1000 ease-out"
            ></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResultChart;