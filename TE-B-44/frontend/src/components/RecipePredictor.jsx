// RecipePredictor.js
import React, { useState } from 'react';
import axios from 'axios';
import '../App.css';

function RecipePredictor() {
    // State hooks for user input, prediction result, loading status, and error handling
    const [ingredients, setIngredients] = useState('');
    const [prediction, setPrediction] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    // Function to send ingredients to the backend and get prediction/match result
    const handlePredict = async () => {
        const trimmed = ingredients.trim();

        // Validate input
        if (!trimmed) {
            setError('Please enter at least one ingredient.');
            return;
        }

        // Reset UI states before sending request
        setLoading(true);
        setPrediction(null);
        setError('');

        try {
            // Send ingredients to the backend
            const response = await axios.post('http://localhost:5000/predict', {
                ingredients: trimmed,
            });

            // Save response data into state
            setPrediction(response.data);
        } catch (err) {
            console.error(err);
            setError('Something went wrong. Please try again later.');
        }

        // Stop loading spinner
        setLoading(false);
    };

    // Reset the form inputs and results
    const handleClear = () => {
        setIngredients('');
        setPrediction(null);
        setError('');
    };

    return (
        <div className="container">
            <h1 className="title">Recipe Predictor</h1>
            <p className="subtitle">Enter ingredients to predict the recipe category and cuisine.</p>

            {/* Ingredients input box */}
            <textarea
                className="input-box"
                rows="5"
                placeholder="e.g. rice, chicken, garlic, onion"
                value={ingredients}
                onChange={(e) => setIngredients(e.target.value)}
            />

            {/* Action buttons: Predict and Clear */}
            <div style={{ marginTop: '10px' }}>
                <button
                    className="predict-btn"
                    onClick={handlePredict}
                    disabled={loading}
                >
                    {loading ? 'Predicting...' : 'Predict'}
                </button>

                <button
                    className="predict-btn"
                    onClick={handleClear}
                    style={{ marginLeft: '10px', backgroundColor: '#aaa' }}
                >
                    Clear
                </button>
            </div>

            {/* Error message if something goes wrong */}
            {error && <p style={{ color: 'red', marginTop: '10px' }}>{error}</p>}

            {/* Show prediction results if available */}
            {prediction && (
                <div className="result-box">
                    <h2>Prediction Result</h2>

                    {/* Case 1: Matching recipes found from dataset using fuzzy matching */}
                    {prediction.source === 'dataset' ? (
                        prediction.matches.length > 0 ? (
                            <div>
                                <p><strong>Found {prediction.matches.length} recipe(s) from dataset:</strong></p>
                                <ul>
                                    {prediction.matches.map((match, idx) => (
                                        <li key={idx} style={{ marginBottom: '15px' }}>
                                            <p><strong>Category:</strong> {match.Category}</p>
                                            <p><strong>Cuisine:</strong> {match.Cuisine}</p>
                                            <p><strong>Matched Ingredients:</strong> {match.MatchedIngredients.join(', ') || 'None'}</p>
                                            <p><strong>All Ingredients:</strong> {match.AllIngredients.join(', ')}</p>
                                            <hr />
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        ) : (
                            <p>No matching recipes found in dataset.</p>
                        )
                    ) : (
                        // Case 2: Prediction from ML model if no match in dataset
                        <div>
                            <p><strong>Category:</strong> {prediction.Category !== 'Unknown' ? prediction.Category : '🤔 Couldn’t determine'}</p>
                            <p><strong>Cuisine:</strong> {prediction.Cuisine !== 'Unknown' ? prediction.Cuisine : '🤔 Couldn’t determine'}</p>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}

export default RecipePredictor;
