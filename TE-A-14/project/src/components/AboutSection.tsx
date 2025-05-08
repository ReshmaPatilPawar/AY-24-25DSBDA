import React from 'react';
import { PieChart, Radar, Binary, Brain } from 'lucide-react';

const AboutSection: React.FC = () => {
  return (
    <section id="about" className="py-12 bg-gray-50">
      <div className="container mx-auto px-6">
        <h2 className="text-3xl font-bold text-center text-blue-900 mb-12">About SONAR Classification</h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div className="bg-white p-6 rounded-lg shadow-md transform transition duration-300 hover:scale-105">
            <div className="flex justify-center mb-4">
              <div className="p-3 bg-blue-100 rounded-full">
                <Radar className="h-8 w-8 text-blue-900" />
              </div>
            </div>
            <h3 className="text-xl font-semibold text-center mb-3 text-blue-800">SONAR Technology</h3>
            <p className="text-gray-600 text-center">
              SONAR (SOund Navigation And Ranging) uses sound waves to detect objects underwater. It's crucial for submarine navigation and underwater object detection.
            </p>
          </div>
          
          <div className="bg-white p-6 rounded-lg shadow-md transform transition duration-300 hover:scale-105">
            <div className="flex justify-center mb-4">
              <div className="p-3 bg-teal-100 rounded-full">
                <PieChart className="h-8 w-8 text-teal-700" />
              </div>
            </div>
            <h3 className="text-xl font-semibold text-center mb-3 text-teal-700">Data Analysis</h3>
            <p className="text-gray-600 text-center">
              Our model analyzes 60 frequency features from SONAR readings to determine if an object is a mine or a rock with high accuracy.
            </p>
          </div>
          
          <div className="bg-white p-6 rounded-lg shadow-md transform transition duration-300 hover:scale-105">
            <div className="flex justify-center mb-4">
              <div className="p-3 bg-orange-100 rounded-full">
                <Brain className="h-8 w-8 text-orange-700" />
              </div>
            </div>
            <h3 className="text-xl font-semibold text-center mb-3 text-orange-700">Machine Learning</h3>
            <p className="text-gray-600 text-center">
              Using Logistic Regression, our model achieved 83% accuracy on training data and 76% on test data for mine versus rock classification.
            </p>
          </div>
          
          <div className="bg-white p-6 rounded-lg shadow-md transform transition duration-300 hover:scale-105">
            <div className="flex justify-center mb-4">
              <div className="p-3 bg-purple-100 rounded-full">
                <Binary className="h-8 w-8 text-purple-700" />
              </div>
            </div>
            <h3 className="text-xl font-semibold text-center mb-3 text-purple-700">Binary Classification</h3>
            <p className="text-gray-600 text-center">
              The model performs binary classification to categorize underwater objects as either mines (dangerous) or rocks (safe).
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;