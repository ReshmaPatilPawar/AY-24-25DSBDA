import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Alert } from 'react-bootstrap';
import DiabetesForm from './components/DiabetesForm';
import PredictionResult from './components/PredictionResult';
import Header from './components/Header';
import InfoSection from './components/InfoSection';

function App() {
  const [predictionResult, setPredictionResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [apiStatus, setApiStatus] = useState({ isChecking: true, isOnline: false, message: 'Checking API status...' });

  // Define the API base URL
  // In production, use environment variable or fall back to relative path
  // In development, use localhost:8000
  const API_BASE_URL = process.env.NODE_ENV === 'production' 
    ? (process.env.REACT_APP_API_URL || '/api')
    : 'http://localhost:8000';

  // Check if the API is available on component mount
  useEffect(() => {
    const checkApiStatus = async () => {
      try {
        console.log('Checking API status at:', `${API_BASE_URL}/health`);
        const response = await fetch(`${API_BASE_URL}/health`);
        console.log('API status response:', response);
        
        if (response.ok) {
          const data = await response.json();
          console.log('API health data:', data);
          setApiStatus({ 
            isChecking: false, 
            isOnline: true, 
            message: 'API is connected' 
          });
        } else {
          setApiStatus({ 
            isChecking: false, 
            isOnline: false, 
            message: 'API is not responding correctly' 
          });
        }
      } catch (err) {
        console.error('API connection error:', err);
        setApiStatus({ 
          isChecking: false, 
          isOnline: false, 
          message: 'Cannot connect to the API server. Make sure the backend is running.' 
        });
      }
    };

    checkApiStatus();
  }, [API_BASE_URL]);

  const handlePrediction = async (formData) => {
    setLoading(true);
    setError(null);
    
    try {
      console.log('Sending prediction request with data:', formData);
      
      const response = await fetch(`${API_BASE_URL}/predict`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      
      console.log('Response status:', response.status);
      
      if (!response.ok) {
        const errorText = await response.text();
        console.error('Error response:', errorText);
        throw new Error(`Failed to get prediction from server: ${response.status} ${response.statusText}`);
      }
      
      const data = await response.json();
      console.log('Prediction result:', data);
      setPredictionResult(data);
    } catch (err) {
      console.error('Error during prediction:', err);
      setError(err.message || 'An error occurred during prediction');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <Header />
      <Container>
        {!apiStatus.isChecking && !apiStatus.isOnline && (
          <Alert variant="danger" className="mt-3">
            {apiStatus.message}
          </Alert>
        )}
        
        <Row className="mb-4">
          <Col>
            <InfoSection />
          </Col>
        </Row>
        <Row>
          <Col md={6}>
            <DiabetesForm 
              onSubmit={handlePrediction} 
              isLoading={loading} 
              isDisabled={!apiStatus.isOnline}
            />
          </Col>
          <Col md={6}>
            <PredictionResult 
              result={predictionResult} 
              loading={loading} 
              error={error} 
            />
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App; 