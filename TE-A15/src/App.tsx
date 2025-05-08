import React, { useState } from 'react';
import { Upload, BarChart, Brain } from 'lucide-react';
import DataUpload from './components/DataUpload';
import DataVisualization from './components/DataVisualization';
import DataPrediction from './components/DataPrediction';

function App() {
  const [activeSection, setActiveSection] = useState<'upload' | 'visualize' | 'predict' | null>(null);
  const [data, setData] = useState<any[]>([]);

  return (
    <div className="min-h-screen bg-white">
      {/* Header */}
      <header className="border-b border-gray-200 py-6">
        <div className="container mx-auto px-4">
          <h1 className="text-2xl font-semibold text-gray-900">Wine Quality Analysis</h1>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        {/* Options Grid */}
        {!activeSection && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <button
              onClick={() => setActiveSection('upload')}
              className="flex flex-col items-center justify-center p-8 border-2 border-gray-200 rounded-lg hover:border-gray-400 transition-colors"
            >
              <Upload className="w-12 h-12 mb-4 text-gray-700" />
              <h2 className="text-xl font-medium text-gray-900">Upload Data</h2>
              <p className="mt-2 text-gray-600 text-center">Import your wine quality dataset for analysis</p>
            </button>

            <button
              onClick={() => setActiveSection('visualize')}
              className="flex flex-col items-center justify-center p-8 border-2 border-gray-200 rounded-lg hover:border-gray-400 transition-colors"
            >
              <BarChart className="w-12 h-12 mb-4 text-gray-700" />
              <h2 className="text-xl font-medium text-gray-900">Visualize Data</h2>
              <p className="mt-2 text-gray-600 text-center">Explore data through interactive charts</p>
            </button>

            <button
              onClick={() => setActiveSection('predict')}
              className="flex flex-col items-center justify-center p-8 border-2 border-gray-200 rounded-lg hover:border-gray-400 transition-colors"
            >
              <Brain className="w-12 h-12 mb-4 text-gray-700" />
              <h2 className="text-xl font-medium text-gray-900">Predict Data</h2>
              <p className="mt-2 text-gray-600 text-center">Get quality predictions for new samples</p>
            </button>
          </div>
        )}

        {/* Active Section */}
        <div className="mt-8">
          {activeSection === 'upload' && (
            <DataUpload onDataUploaded={setData} onBack={() => setActiveSection(null)} />
          )}
          {activeSection === 'visualize' && (
            <DataVisualization data={data} onBack={() => setActiveSection(null)} />
          )}
          {activeSection === 'predict' && (
            <DataPrediction data={data} onBack={() => setActiveSection(null)} />
          )}
        </div>
      </main>
    </div>
  );
}

export default App;