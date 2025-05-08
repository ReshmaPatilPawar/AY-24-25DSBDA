import React from "react";
import PredictionForm from "./PredictionForm";

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 to-blue-50 flex items-center justify-center px-4 py-4">
      <div className="w-full max-w-md mx-4">
        {/* Header */}
        <div className="bg-indigo-600 rounded-t-xl p-4 shadow-md text-center">
          <h1 className="text-2xl font-bold text-white">📱 Phone Addiction Prediction</h1>
          <p className="text-indigo-100 mt-1">Check your phone usage habits</p>
        </div>

        {/* Form and Results */}
        <div className="bg-white p-6 rounded-b-xl shadow-md">
          <PredictionForm />
        </div>

        {/* Footer */}
        <div className="mt-4 text-center text-xs text-gray-500">
          <p>Designed and Developed by Kartik Shingde ❤️</p>
        </div>
      </div>
    </div>
  );
}

export default App;
