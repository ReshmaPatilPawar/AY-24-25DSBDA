import React, { useState } from "react";

const Predict = () => {
  // State to store the input values
  const [formData, setFormData] = useState({
    age: "",
    marriageStatus: "", 
    weight: "",
    bmi: "",
    regularCycle: "", 
    skinDarkening: "",
    hairGrowth: "",
    weightGain: "",
    fastFood: "",
    pimples: "",
  });

  // State to handle error messages
  const [error, setError] = useState("");
  const [response, setResponse] = useState(null);

  // Function to handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Convert lifestyle choice to float (non, mild, heavy, severe)
  const convertLifestyleToFloat = (value) => {
    switch (value) {
      case "non":
        return 0.0;
      case "mild":
        return 0.5;
      case "heavy":
        return 1.0;
      case "severe":
        return 1.5;
      default:
        return 0.0;
    }
  };

  // Convert hair growth to float (No = 0, Yes = 1)
  const convertHairGrowthToFloat = (value) => {
    return value === "Yes" ? 1.0 : 0.0;
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validation: Ensure all fields are filled correctly
    let validationErrors = [];
    let missingFields = [];
    for (const key in formData) {
      if (formData[key] === "") {
        missingFields.push(key);
      }
      const numValue = parseFloat(formData[key]);
      if (
        ["age", "weight", "bmi", "follicleNoR", "follicleNoL", "amh", "cycleLength", "weightGain"].includes(key)
      ) {
        if (isNaN(numValue) || numValue < 0) {
          validationErrors.push(`${key} must be a valid non-negative number.`);
        }
      }
    }

    if (validationErrors.length > 0) {
      setError(validationErrors.join(" "));
      return;
    }

    if (missingFields.length > 0) {
      setError(`Please fill the following fields: ${missingFields.join(", ")}`);
      return;
    }

    // Manually parse form data values as floats, even for integers
    const dataToSend = {
      age: formData.age ? parseFloat(formData.age).toFixed(1) : 0.0, 
      marriageStatus: formData.marriageStatus === "Yes" ? 1.0 : 0.0,
      weight: parseFloat(formData.weight).toFixed(1), 
      bmi: parseFloat(formData.bmi).toFixed(1), 
      follicleNoR: parseFloat(9.0).toFixed(1), 
      follicleNoL: parseFloat(8.0).toFixed(1),
      amh: parseFloat(2.5).toFixed(1),
      regularCycle: formData.regularCycle === "Yes" ? 1.0 : 0.0,
      cycleLength: parseFloat(formData.cycleLength).toFixed(1), 
      skinDarkening: parseFloat(formData.skinDarkening).toFixed(1), 
      hairGrowth: convertHairGrowthToFloat(formData.hairGrowth),
      weightGain: parseFloat(formData.weightGain).toFixed(1), 
      fastFood: convertLifestyleToFloat(formData.fastFood),
      pimples: convertLifestyleToFloat(formData.pimples),
    };

    // Log the request body for debugging
    console.log("Request Body (before sending to backend):", dataToSend);
    console.log("JSON Stringified Request Body:", JSON.stringify(dataToSend));

    // Send the data to the backend
    try {
      const response = await fetch("https://pcos-prediction-backend.onrender.com/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(dataToSend),
      });
      const result = await response.json();
      
      // Log the response for debugging
      console.log("Response from backend:", result);

      // Display the response below the form
      if (result.atRisk) {
        setResponse(<p style={{ color: "red" }}>The patient is at risk.</p>);
      } else {
        setResponse(<p style={{ color: "green" }}>The patient is not at risk.</p>);
      }

      // Clear error message after response
      setError("");
    } catch (err) {
      setError("Failed to submit the data.");
    }
  };

  return (
    <div className="min-h-screen bg-[#fff7f8] w-full flex flex-col justify-center items-center align-middle p-4">
    <div className="font-mono flex flex-col w-full max-w-lg space-y-6">
      <div className="text-center">
        <h1 className="text-4xl md:text-5xl font-bold text-gray-800">Patient Risk Prediction</h1>
      </div>
      <br></br><br></br>
  
  
      <form onSubmit={handleSubmit} className="space-y-6">
        <div className="flex flex-col">
          <label className="text-lg font-semibold text-gray-700">Age (in years):</label>
          <input
            type="number"
            name="age"
            value={formData.age}
            onChange={handleChange}
            step="0.1"
            required
            className="mt-2 p-3 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
  
        <div className="flex flex-col">
          <label className="text-lg font-semibold text-gray-700">Marriage Status (Yes/No):</label>
          <select
            name="marriageStatus"
            value={formData.marriageStatus}
            onChange={handleChange}
            className="mt-2 p-3 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Select</option>
            <option value="Yes">Yes</option>
            <option value="No">No</option>
          </select>
        </div>
  
        <div className="flex flex-col">
          <label className="text-lg font-semibold text-gray-700">Weight (in kg):</label>
          <input
            type="number"
            name="weight"
            value={formData.weight}
            onChange={handleChange}
            step="0.1"
            required
            className="mt-2 p-3 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
  
        <div className="flex flex-col">
          <label className="text-lg font-semibold text-gray-700">BMI:</label>
          <input
            type="number"
            name="bmi"
            value={formData.bmi}
            onChange={handleChange}
            step="0.1"
            required
            className="mt-2 p-3 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        
        <div className="flex flex-col">
          <label className="text-lg font-semibold text-gray-700">Regular Cycle (Yes/No):</label>
          <select
            name="regularCycle"
            value={formData.regularCycle}
            onChange={handleChange}
            className="mt-2 p-3 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Select</option>
            <option value="Yes">Yes</option>
            <option value="No">No</option>
          </select>
        </div>
  
        <div className="flex flex-col">
          <label className="text-lg font-semibold text-gray-700">Cycle Length (in days):</label>
          <input
            type="number"
            name="cycleLength"
            value={formData.cycleLength}
            onChange={handleChange}
            step="1"
            required
            className="mt-2 p-3 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
  
        <div className="flex flex-col">
          <label className="text-lg font-semibold text-gray-700">Skin Darkening (0-1):</label>
          <input
            type="number"
            name="skinDarkening"
            value={formData.skinDarkening}
            onChange={handleChange}
            step="0.1"
            min="0"
            max="1"
            required
            className="mt-2 p-3 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
  
        <div className="flex flex-col">
          <label className="text-lg font-semibold text-gray-700">Hair Growth (Yes/No):</label>
          <select
            name="hairGrowth"
            value={formData.hairGrowth}
            onChange={handleChange}
            className="mt-2 p-3 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Select</option>
            <option value="Yes">Yes</option>
            <option value="No">No</option>
          </select>
        </div>
  
        <div className="flex flex-col">
          <label className="text-lg font-semibold text-gray-700">Weight Gain (in kg):</label>
          <input
            type="number"
            name="weightGain"
            value={formData.weightGain}
            onChange={handleChange}
            step="0.1"
            required
            className="mt-2 p-3 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
  
        <div className="flex flex-col">
          <label className="text-lg font-semibold text-gray-700">Fast Food Intake:</label>
          <select
            name="fastFood"
            value={formData.fastFood}
            onChange={handleChange}
            className="mt-2 p-3 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="non">Non</option>
            <option value="mild">Mild</option>
            <option value="heavy">Heavy</option>
            <option value="severe">Severe</option>
          </select>
        </div>
  
        <div className="flex flex-col">
          <label className="text-lg font-semibold text-gray-700">Pimples:</label>
          <select
            name="pimples"
            value={formData.pimples}
            onChange={handleChange}
            className="mt-2 p-3 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="non">Non</option>
            <option value="mild">Mild</option>
            <option value="heavy">Heavy</option>
            <option value="severe">Severe</option>
          </select>
        </div>
  <br></br>
        <div className="text-center">
          <button
            type="submit"
            className="w-full p-3 bg-blue-500 text-white rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            Submit
          </button>
        </div>
        <br></br>
        {/* Show errors if any */}
      {error && <p className="text-red-500 text-center">{error}</p>}
  
        {/* Show response from the backend */}
        <p className="text-center ">{response}</p>
      </form>
    </div>
  </div>
  
  );
};

export default Predict;
