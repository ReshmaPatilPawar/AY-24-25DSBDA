import React, { useState } from 'react';
import { ArrowLeft } from 'lucide-react';

interface DataPredictionProps {
  data: any[];
  onBack: () => void;
}

const DataPrediction: React.FC<DataPredictionProps> = ({ data, onBack }) => {
  const [prediction, setPrediction] = useState<number | null>(null);
  const [formData, setFormData] = useState({
    'fixed acidity': '',
    'volatile acidity': '',
    'citric acid': '',
    'residual sugar': '',
    'chlorides': '',
    'free sulfur dioxide': '',
    'total sulfur dioxide': '',
    'density': '',
    'pH': '',
    'sulphates': '',
    'alcohol': ''
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    // Simple prediction model (average of similar wines)
    const values = Object.values(formData).map(Number);
    if (values.some(isNaN)) {
      alert('Please fill in all fields with valid numbers');
      return;
    }

    // Calculate average quality of 5 most similar wines
    const similarities = data.map(wine => ({
      quality: wine.quality,
      similarity: Math.sqrt(
        Object.entries(formData).reduce((sum, [key, value]) => {
          const diff = Number(value) - wine[key];
          return sum + diff * diff;
        }, 0)
      )
    }));

    similarities.sort((a, b) => a.similarity - b.similarity);
    const predictedQuality = similarities.slice(0, 5).reduce((sum, s) => sum + s.quality, 0) / 5;
    setPrediction(Math.round(predictedQuality * 10) / 10);
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  return (
    <div>
      <button 
        onClick={onBack}
        className="flex items-center text-gray-600 hover:text-gray-900 mb-6"
      >
        <ArrowLeft className="w-4 h-4 mr-2" />
        Back
      </button>

      <div className="max-w-2xl mx-auto">
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {Object.keys(formData).map(key => (
              <div key={key}>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  {key}
                </label>
                <input
                  type="number"
                  step="0.01"
                  name={key}
                  value={formData[key as keyof typeof formData]}
                  onChange={handleInputChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-gray-900"
                  required
                />
              </div>
            ))}
          </div>

          <button
            type="submit"
            className="w-full px-4 py-2 bg-gray-900 text-white rounded-md hover:bg-gray-800"
          >
            Predict Quality
          </button>
        </form>

        {prediction !== null && (
          <div className="mt-8 p-6 border border-gray-200 rounded-lg">
            <h3 className="text-lg font-medium text-gray-900 mb-2">Predicted Quality</h3>
            <p className="text-3xl font-bold">{prediction}</p>
            <p className="mt-2 text-gray-600">Scale: 0 (very bad) to 10 (excellent)</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default DataPrediction;