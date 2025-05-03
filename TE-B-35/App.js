import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import TransactionForm from './components/TransactionForm';
import ResultCard from './components/ResultCard';
import ExampleCard from './components/ExampleCard';
import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

function App() {
  const [features, setFeatures] = useState([]);
  const [examples, setExamples] = useState({ legitimate: {}, fraudulent: {} });
  const [loading, setLoading] = useState(true);
  const [predictionResult, setPredictionResult] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Get features
        const featuresResponse = await axios.get(`${API_URL}/features`);
        if (featuresResponse.data.features) {
          setFeatures(featuresResponse.data.features);
        }

        // Get example values
        const examplesResponse = await axios.get(`${API_URL}/example-values`);
        if (examplesResponse.data) {
          setExamples({
            legitimate: examplesResponse.data.legitimate,
            fraudulent: examplesResponse.data.fraudulent
          });
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleSubmit = async (formData) => {
    setLoading(true);
    try {
      const response = await axios.post(`${API_URL}/predict`, formData);
      setPredictionResult(response.data);
    } catch (error) {
      console.error('Error making prediction:', error);
      alert('Error making prediction. Please check the console for details.');
    } finally {
      setLoading(false);
    }
  };

  const handleUseExample = (exampleType) => {
    if (examples[exampleType]) {
      handleSubmit(examples[exampleType]);
    }
  };

  return (
    <Container>
      <div className="header">
        <h1>Credit Card Fraud Detection</h1>
        <p className="lead">Enter transaction details to check for potential fraud</p>
      </div>

      <Row>
        <Col md={8}>
          <Card className="mb-4">
            <Card.Header>Transaction Details</Card.Header>
            <Card.Body>
              {loading && features.length === 0 ? (
                <p>Loading transaction form...</p>
              ) : (
                <TransactionForm 
                  features={features} 
                  onSubmit={handleSubmit} 
                  loading={loading}
                />
              )}
            </Card.Body>
          </Card>

          {predictionResult && (
            <ResultCard result={predictionResult} />
          )}
        </Col>

        <Col md={4}>
          <ExampleCard 
            examples={examples} 
            onUseExample={handleUseExample} 
          />
        </Col>
      </Row>
    </Container>
  );
}

export default App; 