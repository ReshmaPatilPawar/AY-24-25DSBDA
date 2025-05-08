import React, { useState, useEffect } from 'react';
import { Target, AlertCircle } from 'lucide-react';

type PredictionResultProps = {
  prediction: string | null;
  confidence: number;
};

const PredictionResult: React.FC<PredictionResultProps> = ({ prediction, confidence }) => {
  const [animate, setAnimate] = useState(false);

  useEffect(() => {
    if (prediction) {
      setAnimate(true);
      const timer = setTimeout(() => setAnimate(false), 1000);
      return () => clearTimeout(timer);
    }
  }, [prediction]);

  if (!prediction) {
    return (
      <div className="bg-gray-100 rounded-lg p-8 text-center flex flex-col items-center">
        <Target className="h-16 w-16 text-gray-400 mb-4" />
        <h3 className="text-lg font-medium text-gray-600">No Prediction Yet</h3>
        <p className="text-gray-500 mt-2">Enter sonar data and click Predict to classify the object</p>
      </div>
    );
  }

  // Determine colors based on prediction
  const isMine = prediction === 'M';
  const bgColor = isMine ? 'bg-red-600' : 'bg-green-600';
  const ringColor = isMine ? 'ring-red-300' : 'ring-green-300';
  const labelText = isMine ? 'Mine Detected' : 'Rock Detected';
  const description = isMine 
    ? 'The object appears to be a mine. Exercise extreme caution!'
    : 'The object appears to be a rock. Likely safe to approach.';

  return (
    <div className={`bg-white rounded-lg shadow-md overflow-hidden transition-all duration-500 ${animate ? 'scale-105' : 'scale-100'}`}>
      <div className={`${bgColor} py-6 px-6 text-white text-center`}>
        <h3 className="text-2xl font-bold">{labelText}</h3>
        <p className="text-white/90 mt-1">{description}</p>
      </div>
      
      <div className="p-6">
        <div className="flex items-center justify-between mb-4">
          <span className="text-gray-700 font-medium">Confidence:</span>
          <span className="font-bold text-blue-900">{(confidence * 100).toFixed(1)}%</span>
        </div>
        
        <div className="h-4 w-full bg-gray-200 rounded-full overflow-hidden">
          <div 
            className={`h-full ${bgColor} transition-all duration-1000 ease-out`}
            style={{ width: `${confidence * 100}%` }}
          />
        </div>
        
        <div className="mt-6 flex items-start">
          <AlertCircle className={`h-5 w-5 ${isMine ? 'text-red-600' : 'text-yellow-600'} mr-2 mt-0.5 flex-shrink-0`} />
          <p className="text-sm text-gray-600">
            {isMine 
              ? 'This classification indicates a potentially dangerous object. The model predicts this is a mine with the confidence level shown above.'
              : 'This classification indicates a likely safe object. However, all predictions should be verified with additional sensing methods.'}
          </p>
        </div>
      </div>
    </div>
  );
};

export default PredictionResult;