import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft, Download, BarChart, Leaf } from 'lucide-react';
import { predictYield } from '../../utils/predictionModel';
import ResultChart from './ResultChart';

const PredictionResult: React.FC = () => {
  const [predictionData, setPredictionData] = useState<any>(null);
  const [result, setResult] = useState<{
    yield: number;
    confidence: number;
    recommendations: string[];
  } | null>(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    // Retrieve prediction data from localStorage
    const storedData = localStorage.getItem('predictionData');
    
    if (storedData) {
      const parsedData = JSON.parse(storedData);
      setPredictionData(parsedData);
      
      // Simulate ML model prediction
      setTimeout(() => {
        const predictionResult = predictYield(parsedData);
        setResult(predictionResult);
        setLoading(false);
      }, 1500);
    } else {
      navigate('/');
    }
  }, [navigate]);

  const handleDownloadReport = () => {
    const reportContent = `
CropYieldAI Prediction Report
-----------------------------
Date: ${new Date().toLocaleDateString()}

FARM INFORMATION
-----------------------------
Crop Type: ${predictionData?.cropType}
Soil Type: ${predictionData?.soilType}
Farming System: ${predictionData?.farmingSystem}
Area: ${predictionData?.area} hectares

ENVIRONMENTAL FACTORS
-----------------------------
Temperature: ${predictionData?.temperature}°C
Humidity: ${predictionData?.humidity}%
Rainfall: ${predictionData?.rainfall} mm
Soil pH: ${predictionData?.ph}

SOIL NUTRIENTS
-----------------------------
Nitrogen (N): ${predictionData?.nitrogen}
Phosphorus (P): ${predictionData?.phosphorus}
Potassium (K): ${predictionData?.potassium}

PREDICTION RESULTS
-----------------------------
Estimated Yield: ${result?.yield} tons/hectare
Prediction Confidence: ${result?.confidence}%

RECOMMENDATIONS
-----------------------------
${result?.recommendations?.join('\n')}
    `;

    const blob = new Blob([reportContent], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'CropYieldAI_Prediction_Report.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center h-64">
        <div className="w-16 h-16 border-t-4 border-green-500 border-solid rounded-full animate-spin"></div>
        <p className="mt-4 text-lg text-gray-700 dark:text-gray-300">Analyzing your data...</p>
      </div>
    );
  }

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 animate-fadeIn">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-white">
          Prediction Results
        </h2>
        <button
          onClick={() => navigate('/')}
          className="flex items-center text-green-600 dark:text-green-400 hover:text-green-700 dark:hover:text-green-300 transition-colors"
        >
          <ArrowLeft className="w-4 h-4 mr-1" />
          <span>Back to Form</span>
        </button>
      </div>

      {result && (
        <>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
            <div className="bg-gray-50 dark:bg-gray-700 p-5 rounded-lg shadow-sm">
              <div className="flex items-center mb-4">
                <Leaf className="w-6 h-6 text-green-600 dark:text-green-400 mr-2" />
                <h3 className="text-lg font-semibold text-gray-800 dark:text-white">
                  Crop Information
                </h3>
              </div>
              <div className="space-y-2">
                <p className="text-gray-700 dark:text-gray-300">
                  <span className="font-medium">Crop Type:</span> {predictionData?.cropType}
                </p>
                <p className="text-gray-700 dark:text-gray-300">
                  <span className="font-medium">Soil Type:</span> {predictionData?.soilType}
                </p>
                <p className="text-gray-700 dark:text-gray-300">
                  <span className="font-medium">Farming System:</span> {predictionData?.farmingSystem}
                </p>
                <p className="text-gray-700 dark:text-gray-300">
                  <span className="font-medium">Area:</span> {predictionData?.area} hectares
                </p>
              </div>
            </div>

            <div className="bg-gray-50 dark:bg-gray-700 p-5 rounded-lg shadow-sm">
              <div className="flex items-center mb-4">
                <BarChart className="w-6 h-6 text-green-600 dark:text-green-400 mr-2" />
                <h3 className="text-lg font-semibold text-gray-800 dark:text-white">
                  Prediction Outcome
                </h3>
              </div>
              <div className="space-y-3">
                <div>
                  <p className="text-sm text-gray-600 dark:text-gray-400 mb-1">Estimated Yield</p>
                  <p className="text-3xl font-bold text-green-600 dark:text-green-400">
                    {result.yield} <span className="text-lg font-normal">tons/hectare</span>
                  </p>
                </div>
                <div>
                  <p className="text-sm text-gray-600 dark:text-gray-400 mb-1">Prediction Confidence</p>
                  <div className="w-full bg-gray-200 dark:bg-gray-600 rounded-full h-4">
                    <div
                      className="bg-green-600 h-4 rounded-full transition-all duration-1000 ease-out"
                      style={{ width: `${result.confidence}%` }}
                    ></div>
                  </div>
                  <p className="text-right text-sm mt-1">{result.confidence}%</p>
                </div>
              </div>
            </div>
          </div>

          <div className="mb-8">
            <ResultChart data={predictionData} yieldValue={result.yield} />
          </div>

          <div className="mb-8">
            <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-3">
              Recommendations
            </h3>
            <ul className="space-y-2 bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
              {result.recommendations.map((recommendation, index) => (
                <li key={index} className="flex items-start">
                  <span className="text-green-600 dark:text-green-400 mr-2">•</span>
                  <span className="text-gray-700 dark:text-gray-300">{recommendation}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="text-center">
            <button
              onClick={handleDownloadReport}
              className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-md shadow-sm
                        focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2
                        transition-colors duration-300 inline-flex items-center"
            >
              <Download className="w-4 h-4 mr-2" />
              Download Report
            </button>
          </div>
        </>
      )}
    </div>
  );
};

export default PredictionResult;