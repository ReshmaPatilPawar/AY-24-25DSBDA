// This is a mock service to simulate the ML backend's prediction logic
// In a real application, this would make an API call to the backend

// Logistic regression weights from the trained model
// Note: These are simplified mock weights for demonstration
const weights = Array(60).fill(0).map(() => Math.random() * 2 - 1);
const bias = -0.2;

export const makePrediction = (inputData: number[]): { prediction: string; confidence: number } => {
  // Ensure we have the correct number of inputs
  if (inputData.length !== 60) {
    throw new Error('Input data must contain exactly 60 features');
  }

  // Simulate logistic regression prediction
  let logit = bias;
  for (let i = 0; i < 60; i++) {
    logit += inputData[i] * weights[i];
  }

  // Apply sigmoid function to get probability
  const probability = 1 / (1 + Math.exp(-logit));
  
  // Predict class based on probability threshold
  const prediction = probability > 0.5 ? 'M' : 'R';
  
  // Calculate confidence (distance from decision boundary)
  const confidence = Math.abs(probability - 0.5) * 2; // Scale to 0-1
  
  return {
    prediction,
    confidence: Math.min(0.95, Math.max(0.6, confidence)) // Clamp between 0.6 and 0.95 for demo
  };
};