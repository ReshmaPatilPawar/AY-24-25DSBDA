import React, { useState, useEffect } from 'react';
import { ArrowLeft } from 'lucide-react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  ScatterChart,
  Scatter,
  LineChart,
  Line
} from 'recharts';

interface DataVisualizationProps {
  data: any[];
  onBack: () => void;
}

const DataVisualization: React.FC<DataVisualizationProps> = ({ data, onBack }) => {
  const [stats, setStats] = useState<any>(null);
  const [qualityDistribution, setQualityDistribution] = useState<any[]>([]);
  const [correlationData, setCorrelationData] = useState<any[]>([]);

  useEffect(() => {
    if (data.length > 0) {
      // Calculate statistics
      const numericColumns = Object.keys(data[0]).filter(key => 
        !isNaN(data[0][key])
      );

      const statistics = numericColumns.reduce((acc: any, column) => {
        const values = data.map(row => row[column]);
        const sum = values.reduce((a: number, b: number) => a + b, 0);
        const mean = sum / values.length;
        const min = Math.min(...values);
        const max = Math.max(...values);

        acc[column] = {
          mean: mean.toFixed(2),
          min: min.toFixed(2),
          max: max.toFixed(2),
        };
        return acc;
      }, {});

      setStats(statistics);

      // Calculate quality distribution
      const distribution = data.reduce((acc: any, row) => {
        const quality = row.quality;
        acc[quality] = (acc[quality] || 0) + 1;
        return acc;
      }, {});

      setQualityDistribution(
        Object.entries(distribution).map(([quality, count]) => ({
          quality: Number(quality),
          count
        }))
      );

      // Prepare correlation data (alcohol vs quality)
      setCorrelationData(
        data.map(row => ({
          alcohol: row.alcohol,
          quality: row.quality
        }))
      );
    }
  }, [data]);

  if (data.length === 0) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-600">Please upload data first to visualize statistics</p>
      </div>
    );
  }

  return (
    <div>
      <button 
        onClick={onBack}
        className="flex items-center text-gray-600 hover:text-gray-900 mb-6"
      >
        <ArrowLeft className="w-4 h-4 mr-2" />
        Back
      </button>

      <div className="space-y-8">
        {/* Quality Distribution Chart */}
        <div className="bg-white p-6 rounded-lg border border-gray-200">
          <h3 className="text-lg font-medium text-gray-900 mb-4">Wine Quality Distribution</h3>
          <div className="h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={qualityDistribution}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="quality" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="count" fill="#111827" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Alcohol vs Quality Correlation */}
        <div className="bg-white p-6 rounded-lg border border-gray-200">
          <h3 className="text-lg font-medium text-gray-900 mb-4">Alcohol Content vs Quality Correlation</h3>
          <div className="h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <ScatterChart>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="alcohol" name="Alcohol (%)" />
                <YAxis dataKey="quality" name="Quality" />
                <Tooltip cursor={{ strokeDasharray: '3 3' }} />
                <Scatter name="Wines" data={correlationData} fill="#111827" />
              </ScatterChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Statistics Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {stats && Object.entries(stats).map(([column, values]: [string, any]) => (
            <div key={column} className="border border-gray-200 rounded-lg p-6">
              <h3 className="text-lg font-medium text-gray-900 mb-4">{column}</h3>
              <dl className="space-y-2">
                <div className="flex justify-between">
                  <dt className="text-gray-600">Mean:</dt>
                  <dd className="font-medium">{values.mean}</dd>
                </div>
                <div className="flex justify-between">
                  <dt className="text-gray-600">Min:</dt>
                  <dd className="font-medium">{values.min}</dd>
                </div>
                <div className="flex justify-between">
                  <dt className="text-gray-600">Max:</dt>
                  <dd className="font-medium">{values.max}</dd>
                </div>
              </dl>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default DataVisualization;