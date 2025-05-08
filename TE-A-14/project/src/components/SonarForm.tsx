import React, { useState } from 'react';
import { AlertCircle } from 'lucide-react';

// Sample data from the notebook
const SAMPLE_MINE = [0.0307,0.0523,0.0653,0.0521,0.0611,0.0577,0.0665,0.0664,0.1460,0.2792,0.3877,0.4992,0.4981,0.4972,0.5607,0.7339,0.8230,0.9173,0.9975,0.9911,0.8240,0.6498,0.5980,0.4862,0.3150,0.1543,0.0989,0.0284,0.1008,0.2636,0.2694,0.2930,0.2925,0.3998,0.3660,0.3172,0.4609,0.4374,0.1820,0.3376,0.6202,0.4448,0.1863,0.1420,0.0589,0.0576,0.0672,0.0269,0.0245,0.0190,0.0063,0.0321,0.0189,0.0137,0.0277,0.0152,0.0052,0.0121,0.0124,0.0055];

const SAMPLE_ROCK = [0.0453,0.0523,0.0843,0.0689,0.1183,0.2583,0.2156,0.3481,0.3337,0.2872,0.4918,0.6552,0.6919,0.7797,0.7464,0.9444,1.0000,0.8874,0.8024,0.7818,0.5212,0.4052,0.3957,0.3914,0.3250,0.3200,0.3271,0.2767,0.4423,0.2028,0.3788,0.2947,0.1984,0.2341,0.1306,0.4182,0.3835,0.1057,0.1840,0.1970,0.1674,0.0583,0.1401,0.1628,0.0621,0.0203,0.0530,0.0742,0.0409,0.0061,0.0125,0.0084,0.0089,0.0048,0.0094,0.0191,0.0140,0.0049,0.0052,0.0044];

type FormProps = {
  onPredict: (data: number[]) => void;
};

const SonarForm: React.FC<FormProps> = ({ onPredict }) => {
  const [formMode, setFormMode] = useState<'simple' | 'advanced'>('simple');
  const [inputData, setInputData] = useState<string>('');
  const [error, setError] = useState<string | null>(null);

  const handlePredictClick = () => {
    try {
      if (!inputData.trim()) {
        setError('Please enter data or select a sample');
        return;
      }

      // Parse the input data
      const parsedData = inputData
        .split(',')
        .map(val => parseFloat(val.trim()));

      // Validate data
      if (parsedData.length !== 60) {
        setError(`Expected 60 values, got ${parsedData.length}`);
        return;
      }

      if (parsedData.some(isNaN)) {
        setError('Invalid data format. All values must be numbers.');
        return;
      }

      setError(null);
      onPredict(parsedData);
    } catch (err) {
      setError('Error processing data. Please check the format.');
    }
  };

  const loadSample = (sample: number[]) => {
    setInputData(sample.join(', '));
    setError(null);
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6 mb-8">
      <h2 className="text-xl font-bold mb-4 text-blue-900">Input SONAR Data</h2>

      <div className="mb-4">
        <div className="flex justify-between mb-2">
          <div className="flex space-x-2">
            <button
              className={`px-3 py-1 rounded-md text-sm ${
                formMode === 'simple' ? 'bg-blue-900 text-white' : 'bg-gray-200 text-gray-700'
              }`}
              onClick={() => setFormMode('simple')}
            >
              Simple Input
            </button>
            <button
              className={`px-3 py-1 rounded-md text-sm ${
                formMode === 'advanced' ? 'bg-blue-900 text-white' : 'bg-gray-200 text-gray-700'
              }`}
              onClick={() => setFormMode('advanced')}
            >
              Advanced Input
            </button>
          </div>
          <div className="flex space-x-2">
            <button
              className="text-sm px-3 py-1 bg-teal-600 text-white rounded-md hover:bg-teal-700 transition-colors"
              onClick={() => loadSample(SAMPLE_MINE)}
            >
              Load Mine Example
            </button>
            <button
              className="text-sm px-3 py-1 bg-orange-500 text-white rounded-md hover:bg-orange-600 transition-colors"
              onClick={() => loadSample(SAMPLE_ROCK)}
            >
              Load Rock Example
            </button>
          </div>
        </div>

        {formMode === 'simple' ? (
          <textarea
            className="w-full h-32 p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
            placeholder="Enter 60 comma-separated values (e.g., 0.0307, 0.0523, ...)"
            value={inputData}
            onChange={(e) => setInputData(e.target.value)}
          />
        ) : (
          <div className="grid grid-cols-6 gap-2">
            {Array.from({ length: 60 }).map((_, index) => {
              const value = inputData.split(',')[index]?.trim() || '';
              return (
                <input
                  key={index}
                  type="text"
                  placeholder={`Value ${index + 1}`}
                  className="p-2 border border-gray-300 rounded-md text-sm"
                  value={value}
                  onChange={(e) => {
                    const values = inputData.split(',');
                    values[index] = e.target.value;
                    setInputData(values.join(','));
                  }}
                />
              );
            })}
          </div>
        )}

        {error && (
          <div className="mt-2 text-red-600 flex items-center text-sm">
            <AlertCircle className="h-4 w-4 mr-1" />
            {error}
          </div>
        )}
      </div>

      <div className="flex justify-center">
        <button
          className="px-6 py-2 bg-blue-900 text-white rounded-md hover:bg-blue-800 transition-colors font-medium"
          onClick={handlePredictClick}
        >
          Predict
        </button>
      </div>
    </div>
  );
};

export default SonarForm;