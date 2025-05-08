import React, { useState } from 'react';
import InputField from './InputField';
import SelectField from './SelectField';
import { soilTypes, cropTypes, farmingSystems } from '../../data/formOptions';
import { useNavigate } from 'react-router-dom';

interface FormData {
  cropType: string;
  soilType: string;
  farmingSystem: string;
  area: number;
  temperature: number;
  humidity: number;
  rainfall: number;
  nitrogen: number;
  phosphorus: number;
  potassium: number;
  ph: number;
}

const initialFormData: FormData = {
  cropType: '',
  soilType: '',
  farmingSystem: '',
  area: 1,
  temperature: 25,
  humidity: 60,
  rainfall: 100,
  nitrogen: 50,
  phosphorus: 50,
  potassium: 50,
  ph: 7,
};

const PredictionForm: React.FC = () => {
  const [formData, setFormData] = useState<FormData>(initialFormData);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSelectChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    
    // Simulate API call/processing time
    setTimeout(() => {
      setLoading(false);
      // Store form data in localStorage to access in results page
      localStorage.setItem('predictionData', JSON.stringify(formData));
      // Navigate to results page
      navigate('/results');
    }, 1500);
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 transition-all duration-300 transform hover:shadow-lg">
      <h2 className="text-2xl font-bold text-gray-800 dark:text-white mb-6">
        Crop Yield Prediction
      </h2>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <SelectField
            id="cropType"
            label="Crop Type"
            value={formData.cropType}
            options={cropTypes}
            onChange={handleSelectChange}
            required
            helpText="Select the type of crop you are planning to grow"
          />
          
          <SelectField
            id="soilType"
            label="Soil Type"
            value={formData.soilType}
            options={soilTypes}
            onChange={handleSelectChange}
            required
            helpText="Select the type of soil in your farm"
          />
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <SelectField
            id="farmingSystem"
            label="Farming System"
            value={formData.farmingSystem}
            options={farmingSystems}
            onChange={handleSelectChange}
            required
            helpText="Select the farming system you are using"
          />
          
          <InputField
            id="area"
            label="Area (hectares)"
            type="number"
            value={formData.area}
            min={0.1}
            step={0.1}
            onChange={handleInputChange}
            required
            helpText="Enter the area of your farm in hectares"
          />
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <InputField
            id="temperature"
            label="Average Temperature (°C)"
            type="number"
            value={formData.temperature}
            min={-10}
            max={50}
            step={0.1}
            onChange={handleInputChange}
            required
            helpText="Enter the average temperature in degrees Celsius"
          />
          
          <InputField
            id="humidity"
            label="Average Humidity (%)"
            type="number"
            value={formData.humidity}
            min={0}
            max={100}
            step={1}
            onChange={handleInputChange}
            required
            helpText="Enter the average humidity percentage"
          />
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <InputField
            id="rainfall"
            label="Annual Rainfall (mm)"
            type="number"
            value={formData.rainfall}
            min={0}
            step={1}
            onChange={handleInputChange}
            required
            helpText="Enter the annual rainfall in millimeters"
          />
          
          <InputField
            id="ph"
            label="Soil pH Level"
            type="number"
            value={formData.ph}
            min={0}
            max={14}
            step={0.1}
            onChange={handleInputChange}
            required
            helpText="Enter the soil pH level (0-14)"
          />
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <InputField
            id="nitrogen"
            label="Nitrogen (N) Content"
            type="number"
            value={formData.nitrogen}
            min={0}
            max={100}
            step={1}
            onChange={handleInputChange}
            required
            helpText="Nitrogen content in the soil (0-100)"
          />
          
          <InputField
            id="phosphorus"
            label="Phosphorus (P) Content"
            type="number"
            value={formData.phosphorus}
            min={0}
            max={100}
            step={1}
            onChange={handleInputChange}
            required
            helpText="Phosphorus content in the soil (0-100)"
          />
          
          <InputField
            id="potassium"
            label="Potassium (K) Content"
            type="number"
            value={formData.potassium}
            min={0}
            max={100}
            step={1}
            onChange={handleInputChange}
            required
            helpText="Potassium content in the soil (0-100)"
          />
        </div>
        
        <div className="mt-6 text-center">
          <button
            type="submit"
            disabled={loading}
            className="px-6 py-3 bg-green-600 hover:bg-green-700 text-white rounded-md shadow-sm
                      focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2
                      transition-colors duration-300 flex items-center justify-center space-x-2 w-full md:w-auto md:mx-auto"
          >
            {loading ? (
              <>
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span>Processing...</span>
              </>
            ) : (
              <span>Predict Yield</span>
            )}
          </button>
        </div>
      </form>
    </div>
  );
};

export default PredictionForm;