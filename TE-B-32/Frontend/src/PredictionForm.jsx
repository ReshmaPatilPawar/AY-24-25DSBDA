import React, { useState } from "react";
import axios from "axios";

const InputField = ({ label, name, value, onChange, placeholder }) => (
  <div>
    <label className="block text-sm font-medium text-gray-700 mb-1">
      {label}
    </label>
    <input
      type="number"
      name={name}
      value={value}
      onChange={onChange}
      step="0.1"
      placeholder={placeholder}
      required
      className="w-full p-3 text-base border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
    />
  </div>
);

const PredictionForm = () => {
  const [form, setForm] = useState({
    screen_time: "",
    data_usage: "",
    social_media_time: "",
    gaming_time: "",
  });

  const [result, setResult] = useState("");
  const [adviceList, setAdviceList] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const screen = parseFloat(form.screen_time || 0);
    const social = parseFloat(form.social_media_time || 0);
    const gaming = parseFloat(form.gaming_time || 0);

    setLoading(true);
    setResult("");
    setAdviceList([]);

    try {
      const response = await axios.post(
        "https://dsbda-backend.onrender.com/predict",
        form
      );

      setTimeout(() => {
        setLoading(false);
        const level = response.data.result;

        if (level === "Addicted") {
          setResult("✅ You are addicted to phone usage. 📱🔥");

          const tips = [
            screen > 6 && "🕒 Try reducing your overall screen time.👍",
            social > 3 && "📱 Spend less time on social media apps.👍",
            gaming > 2 && "🎮 Reduce your gaming time slightly.👍",
          ].filter(Boolean);

          setAdviceList(
            tips.length ? tips : ["💡 Try maintaining a balance in your routine.👍"]
          );
        } else {
          setResult("✅ You are not addicted to phone usage. 👍");
        }
      }, 700);
    } catch (error) {
      setLoading(false);
      setResult("❌ Error: " + error.message);
    }
  };

  return (
    <>
      <form onSubmit={handleSubmit} className="space-y-4">
        <InputField
          label="Screen Time (hrs)"
          name="screen_time"
          value={form.screen_time}
          onChange={handleChange}
          placeholder="Enter screen time"
        />
        <InputField
          label="Data Usage (GB)"
          name="data_usage"
          value={form.data_usage}
          onChange={handleChange}
          placeholder="Enter data usage"
        />
        <InputField
          label="Social Media Time (hrs)"
          name="social_media_time"
          value={form.social_media_time}
          onChange={handleChange}
          placeholder="Enter social media time"
        />
        <InputField
          label="Gaming Time (hrs)"
          name="gaming_time"
          value={form.gaming_time}
          onChange={handleChange}
          placeholder="Enter gaming time"
        />

        <button
          type="submit"
          className="w-full bg-indigo-600 text-white py-3 px-4 rounded-lg text-base font-semibold shadow-md hover:bg-indigo-700 transition duration-300 mt-6 cursor-pointer"
        >
          Predict Addiction Level
        </button>
      </form>

      {/* Results Section */}
      <div className="mt-6">
        {loading && (
          <div className="text-center py-4">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-indigo-600 mb-2"></div>
            <p className="text-indigo-600 font-medium">🤖 Predicting using Trained Model...</p>
          </div>
        )}

        {!loading && result && (
          <div
            className={`rounded-lg p-4 ${
              result.includes("not addicted") ? "bg-green-50" : "bg-red-50"
            }`}
          >
            <h3
              className={`text-lg font-bold ${
                result.includes("Error")
                  ? "text-red-600"
                  : result.includes("not addicted")
                  ? "text-green-600"
                  : "text-red-500"
              }`}
            >
              {result}
            </h3>

            {adviceList.length > 0 && (
              <div className="mt-3">
                <p className="text-gray-800 mb-2 font-semibold">
                  💡 Here's some advice:
                </p>
                <ul className="space-y-2 pl-5">
                  {adviceList.map((tip, index) => (
                    <li key={index} className="list-disc text-gray-700">
                      {tip}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}
      </div>
    </>
  );
};

export default PredictionForm;
