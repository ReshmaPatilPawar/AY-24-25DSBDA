import React, { useState } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import SonarForm from './components/SonarForm';
import PredictionResult from './components/PredictionResult';
import AboutSection from './components/AboutSection';
import HowItWorks from './components/HowItWorks';
import ModelMetrics from './components/ModelMetrics';
import { makePrediction } from './services/predictionService';

function App() {
  const [prediction, setPrediction] = useState<string | null>(null);
  const [confidence, setConfidence] = useState<number>(0);

  const handlePredict = (data: number[]) => {
    try {
      // In a real app, this would call a backend API
      const result = makePrediction(data);
      setPrediction(result.prediction);
      setConfidence(result.confidence);
    } catch (error) {
      console.error('Prediction error:', error);
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <Header />
      
      <main className="flex-grow">
        {/* Hero Section */}
        <section className="bg-gradient-to-b from-blue-900 to-blue-800 text-white py-16">
          <div className="container mx-auto px-6 text-center">
            <h1 className="text-4xl md:text-5xl font-bold mb-4">SONAR Object Classification</h1>
            <p className="text-xl md:text-2xl mb-8 text-blue-100">
              Detect mines and rocks underwater using machine learning
            </p>
            <div className="max-w-md mx-auto">
              <a 
                href="#classifier"
                className="inline-block bg-teal-500 hover:bg-teal-600 text-white font-bold py-3 px-6 rounded-lg shadow-lg transform transition hover:scale-105 duration-200"
              >
                Try The Classifier
              </a>
            </div>
          </div>
        </section>
        
        {/* Classifier Section */}
        <section id="classifier" className="py-16">
          <div className="container mx-auto px-6">
            <h2 className="text-3xl font-bold text-center text-blue-900 mb-12">
              SONAR Object Classifier
            </h2>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <SonarForm onPredict={handlePredict} />
              <PredictionResult prediction={prediction} confidence={confidence} />
            </div>
          </div>
        </section>
        
        {/* About Section */}
        <AboutSection />
        
        {/* How It Works Section */}
        <HowItWorks />
        
        {/* Model Metrics Section */}
        <ModelMetrics />
      </main>
      
      <Footer />
    </div>
  );
}

export default App;