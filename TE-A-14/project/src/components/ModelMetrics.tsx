import React, { useState } from 'react';
import { BarChart, PieChart } from 'lucide-react';

const ModelMetrics: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'accuracy' | 'confusion'>('accuracy');
  
  return (
    <section className="py-10 bg-white">
      <div className="container mx-auto px-6">
        <h2 className="text-2xl font-bold text-blue-900 mb-6">Model Performance Metrics</h2>
        
        <div className="flex space-x-4 mb-6">
          <button
            className={`flex items-center px-4 py-2 rounded-md ${
              activeTab === 'accuracy' 
                ? 'bg-blue-900 text-white' 
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            } transition-colors`}
            onClick={() => setActiveTab('accuracy')}
          >
            <BarChart className="h-4 w-4 mr-2" />
            Accuracy Metrics
          </button>
          <button
            className={`flex items-center px-4 py-2 rounded-md ${
              activeTab === 'confusion' 
                ? 'bg-blue-900 text-white' 
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            } transition-colors`}
            onClick={() => setActiveTab('confusion')}
          >
            <PieChart className="h-4 w-4 mr-2" />
            Confusion Matrix
          </button>
        </div>
        
        {activeTab === 'accuracy' ? (
          <div className="bg-white rounded-lg shadow-md p-6 animate-fadeIn">
            <h3 className="text-lg font-semibold mb-4 text-blue-800">Model Accuracy</h3>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div>
                <h4 className="text-sm font-medium text-gray-600 mb-2">Training Accuracy</h4>
                <div className="h-6 w-full bg-gray-200 rounded-full overflow-hidden">
                  <div 
                    className="h-full bg-green-600 transition-all duration-1000 ease-out"
                    style={{ width: '83.4%' }}
                  />
                </div>
                <div className="flex justify-between mt-1">
                  <span className="text-xs text-gray-600">0%</span>
                  <span className="text-xs font-semibold text-gray-700">83.4%</span>
                  <span className="text-xs text-gray-600">100%</span>
                </div>
              </div>
              
              <div>
                <h4 className="text-sm font-medium text-gray-600 mb-2">Test Accuracy</h4>
                <div className="h-6 w-full bg-gray-200 rounded-full overflow-hidden">
                  <div 
                    className="h-full bg-blue-600 transition-all duration-1000 ease-out"
                    style={{ width: '76.2%' }}
                  />
                </div>
                <div className="flex justify-between mt-1">
                  <span className="text-xs text-gray-600">0%</span>
                  <span className="text-xs font-semibold text-gray-700">76.2%</span>
                  <span className="text-xs text-gray-600">100%</span>
                </div>
              </div>
            </div>
            
            <div className="mt-8">
              <h4 className="text-sm font-medium text-gray-600 mb-3">Class Distribution</h4>
              <div className="flex space-x-4">
                <div className="flex-1 bg-gray-100 p-4 rounded-md">
                  <div className="flex justify-between items-center mb-2">
                    <span className="text-sm font-medium text-gray-700">Mines (M)</span>
                    <span className="text-sm font-semibold text-blue-900">111 samples</span>
                  </div>
                  <div className="h-4 w-full bg-gray-200 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-red-500 transition-all duration-1000 ease-out"
                      style={{ width: `${(111/208)*100}%` }}
                    />
                  </div>
                  <div className="text-right mt-1">
                    <span className="text-xs text-gray-600">53.4%</span>
                  </div>
                </div>
                
                <div className="flex-1 bg-gray-100 p-4 rounded-md">
                  <div className="flex justify-between items-center mb-2">
                    <span className="text-sm font-medium text-gray-700">Rocks (R)</span>
                    <span className="text-sm font-semibold text-blue-900">97 samples</span>
                  </div>
                  <div className="h-4 w-full bg-gray-200 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-green-500 transition-all duration-1000 ease-out"
                      style={{ width: `${(97/208)*100}%` }}
                    />
                  </div>
                  <div className="text-right mt-1">
                    <span className="text-xs text-gray-600">46.6%</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ) : (
          <div className="bg-white rounded-lg shadow-md p-6 animate-fadeIn">
            <h3 className="text-lg font-semibold mb-4 text-blue-800">Confusion Matrix</h3>
            
            <div className="max-w-md mx-auto">
              <div className="grid grid-cols-[auto,1fr,1fr] gap-1">
                {/* Header row */}
                <div className="bg-gray-100 p-3"></div>
                <div className="bg-gray-100 p-3 text-center font-medium text-gray-700">Predicted Rock</div>
                <div className="bg-gray-100 p-3 text-center font-medium text-gray-700">Predicted Mine</div>
                
                {/* Actual Rock row */}
                <div className="bg-gray-100 p-3 font-medium text-gray-700">Actual Rock</div>
                <div className="bg-green-100 p-3 text-center">
                  <span className="text-lg font-bold text-green-800">74</span>
                  <span className="text-xs block text-green-700">True Negative</span>
                </div>
                <div className="bg-red-100 p-3 text-center">
                  <span className="text-lg font-bold text-red-800">23</span>
                  <span className="text-xs block text-red-700">False Positive</span>
                </div>
                
                {/* Actual Mine row */}
                <div className="bg-gray-100 p-3 font-medium text-gray-700">Actual Mine</div>
                <div className="bg-red-100 p-3 text-center">
                  <span className="text-lg font-bold text-red-800">31</span>
                  <span className="text-xs block text-red-700">False Negative</span>
                </div>
                <div className="bg-green-100 p-3 text-center">
                  <span className="text-lg font-bold text-green-800">80</span>
                  <span className="text-xs block text-green-700">True Positive</span>
                </div>
              </div>
            </div>
            
            <div className="mt-6 text-sm text-gray-600 max-w-2xl mx-auto bg-blue-50 p-4 rounded-md">
              <p className="mb-2">
                <span className="font-medium">Interpreting the Confusion Matrix:</span>
              </p>
              <ul className="list-disc pl-5 space-y-1">
                <li><span className="font-medium">True Positive:</span> Correctly identified mines</li>
                <li><span className="font-medium">True Negative:</span> Correctly identified rocks</li>
                <li><span className="font-medium">False Positive:</span> Rocks incorrectly classified as mines</li>
                <li><span className="font-medium">False Negative:</span> Mines incorrectly classified as rocks</li>
              </ul>
              <p className="mt-2">
                <span className="text-red-600 font-medium">Note:</span> False negatives (missed mines) are particularly dangerous in real-world applications.
              </p>
            </div>
          </div>
        )}
      </div>
    </section>
  );
};

export default ModelMetrics;