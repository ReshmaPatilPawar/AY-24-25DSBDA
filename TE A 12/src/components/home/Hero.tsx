import React from 'react';
import { Sprout, LineChart, FileText } from 'lucide-react';

const Hero: React.FC = () => {
  return (
    <div className="py-12 md:py-16 text-center">
      <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-4">
        Predict Your <span className="text-green-600 dark:text-green-400">Crop Yield</span> with AI
      </h1>
      <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto mb-10">
        Use advanced machine learning to forecast your agricultural yields based on environmental conditions and farming practices.
      </p>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto mb-12">
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md transition-transform duration-300 hover:transform hover:scale-105">
          <div className="flex justify-center mb-4">
            <div className="p-3 bg-green-100 dark:bg-green-900 rounded-full">
              <Sprout className="h-8 w-8 text-green-600 dark:text-green-400" />
            </div>
          </div>
          <h3 className="text-xl font-semibold text-gray-800 dark:text-white mb-2">Smart Analysis</h3>
          <p className="text-gray-600 dark:text-gray-300">
            Our AI analyzes soil conditions, climate data, and farming practices to provide accurate yield predictions.
          </p>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md transition-transform duration-300 hover:transform hover:scale-105">
          <div className="flex justify-center mb-4">
            <div className="p-3 bg-green-100 dark:bg-green-900 rounded-full">
              <LineChart className="h-8 w-8 text-green-600 dark:text-green-400" />
            </div>
          </div>
          <h3 className="text-xl font-semibold text-gray-800 dark:text-white mb-2">Data Visualization</h3>
          <p className="text-gray-600 dark:text-gray-300">
            View comprehensive charts and statistics to understand the factors affecting your crop yield potential.
          </p>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md transition-transform duration-300 hover:transform hover:scale-105">
          <div className="flex justify-center mb-4">
            <div className="p-3 bg-green-100 dark:bg-green-900 rounded-full">
              <FileText className="h-8 w-8 text-green-600 dark:text-green-400" />
            </div>
          </div>
          <h3 className="text-xl font-semibold text-gray-800 dark:text-white mb-2">Actionable Insights</h3>
          <p className="text-gray-600 dark:text-gray-300">
            Receive tailored recommendations to optimize your farming practices and maximize your yields.
          </p>
        </div>
      </div>
      
      <a
        href="#prediction-form"
        className="inline-block px-6 py-3 bg-green-600 hover:bg-green-700 text-white rounded-md shadow
                  focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2
                  transition-colors duration-300 animate-bounce"
      >
        Start Predicting Now
      </a>
    </div>
  );
};

export default Hero;