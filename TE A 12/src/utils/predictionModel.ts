// This is a simplified simulation of an ML model
// In a real application, this would likely be an API call to a backend ML service

interface PredictionInput {
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

interface PredictionOutput {
  yield: number;
  confidence: number;
  recommendations: string[];
}

// Baseline yields for different crops in tons per hectare
const baselineYields: Record<string, number> = {
  rice: 4.5,
  wheat: 3.5,
  maize: 5.5,
  soybean: 2.8,
  potato: 25.0,
  tomato: 35.0,
  cotton: 2.0,
  sugarcane: 70.0,
  '': 4.0, // default
};

// Simulate ML prediction
export const predictYield = (input: PredictionInput): PredictionOutput => {
  // Start with baseline yield for the crop type
  let baseYield = baselineYields[input.cropType] || baselineYields[''];
  
  // Soil type modifier
  const soilModifiers: Record<string, number> = {
    loamy: 1.15,
    clay: 0.9,
    sandy: 0.8,
    silt: 1.1,
    peaty: 1.05,
    chalky: 0.85,
    black: 1.2,
    red: 1.0,
    '': 1.0,
  };
  
  // Farming system modifier
  const farmingSystemModifiers: Record<string, number> = {
    conventional: 1.0,
    organic: 0.85,
    conservation: 1.05,
    precision: 1.25,
    integrated: 1.15,
    hydroponics: 1.4,
    agroforestry: 0.95,
    '': 1.0,
  };
  
  // Apply modifiers
  let yieldValue = baseYield;
  yieldValue *= soilModifiers[input.soilType] || 1.0;
  yieldValue *= farmingSystemModifiers[input.farmingSystem] || 1.0;
  
  // Apply temperature effect (optimal range varies by crop)
  const tempFactor = getTemperatureFactor(input.cropType, input.temperature);
  yieldValue *= tempFactor;
  
  // Apply rainfall/humidity factors
  const waterFactor = getWaterFactor(input.cropType, input.rainfall, input.humidity);
  yieldValue *= waterFactor;
  
  // Apply nutrient factors
  const nutrientFactor = getNutrientFactor(input.nitrogen, input.phosphorus, input.potassium);
  yieldValue *= nutrientFactor;
  
  // Apply pH factor
  const phFactor = getPHFactor(input.cropType, input.ph);
  yieldValue *= phFactor;
  
  // Simulate some randomness (in a real model, this would be more sophisticated)
  const randomVariation = 0.9 + (Math.random() * 0.2); // 0.9 to 1.1
  yieldValue *= randomVariation;
  
  // Round to 2 decimal places
  yieldValue = Math.round(yieldValue * 100) / 100;
  
  // Calculate confidence (simplified)
  const confidence = calculateConfidence(input);
  
  // Generate recommendations
  const recommendations = generateRecommendations(input, yieldValue);
  
  return {
    yield: yieldValue,
    confidence,
    recommendations,
  };
};

// Helper functions
function getTemperatureFactor(cropType: string, temperature: number): number {
  // Different crops have different optimal temperature ranges
  const optimalTemps: Record<string, [number, number]> = {
    rice: [25, 30],
    wheat: [15, 20],
    maize: [20, 25],
    soybean: [20, 30],
    potato: [15, 20],
    tomato: [20, 25],
    cotton: [25, 30],
    sugarcane: [25, 35],
  };
  
  const [min, max] = optimalTemps[cropType] || [20, 25];
  
  if (temperature >= min && temperature <= max) {
    return 1.0; // Optimal
  } else if (temperature < min) {
    return 1.0 - ((min - temperature) * 0.05); // Too cold
  } else {
    return 1.0 - ((temperature - max) * 0.04); // Too hot
  }
}

function getWaterFactor(cropType: string, rainfall: number, humidity: number): number {
  // Different crops have different water requirements
  const optimalRainfall: Record<string, number> = {
    rice: 1200,
    wheat: 600,
    maize: 700,
    soybean: 600,
    potato: 500,
    tomato: 600,
    cotton: 800,
    sugarcane: 1500,
  };
  
  const optimal = optimalRainfall[cropType] || 700;
  let factor = 1.0;
  
  // Adjust based on rainfall
  if (rainfall < optimal) {
    factor *= (0.7 + (rainfall / optimal) * 0.3);
  } else if (rainfall > optimal * 1.5) {
    factor *= (1.0 - ((rainfall - optimal * 1.5) / optimal) * 0.2);
  }
  
  // Adjust based on humidity
  if (humidity < 40) {
    factor *= 0.9;
  } else if (humidity > 80) {
    factor *= 0.95;
  }
  
  return factor;
}

function getNutrientFactor(nitrogen: number, phosphorus: number, potassium: number): number {
  // Simple nutrient model
  const nFactor = 0.7 + (nitrogen / 100) * 0.3;
  const pFactor = 0.8 + (phosphorus / 100) * 0.2;
  const kFactor = 0.8 + (potassium / 100) * 0.2;
  
  return (nFactor + pFactor + kFactor) / 3;
}

function getPHFactor(cropType: string, ph: number): number {
  // Different crops have different pH preferences
  const optimalPH: Record<string, [number, number]> = {
    rice: [5.5, 6.5],
    wheat: [6.0, 7.0],
    maize: [5.8, 7.0],
    soybean: [6.0, 6.8],
    potato: [5.0, 6.0],
    tomato: [6.0, 6.8],
    cotton: [5.8, 8.0],
    sugarcane: [6.0, 7.5],
  };
  
  const [min, max] = optimalPH[cropType] || [6.0, 7.0];
  
  if (ph >= min && ph <= max) {
    return 1.0; // Optimal
  } else if (ph < min) {
    return 1.0 - ((min - ph) * 0.1); // Too acidic
  } else {
    return 1.0 - ((ph - max) * 0.08); // Too alkaline
  }
}

function calculateConfidence(input: PredictionInput): number {
  // In a real system, this would be based on model uncertainty
  // This is a simplified version
  
  let confidence = 80; // Base confidence
  
  // Reduce confidence for extremes
  if (input.temperature < 5 || input.temperature > 40) confidence -= 10;
  if (input.rainfall < 200 || input.rainfall > 3000) confidence -= 15;
  if (input.ph < 4 || input.ph > 9) confidence -= 10;
  
  // Reduce confidence for empty selections
  if (!input.cropType) confidence -= 25;
  if (!input.soilType) confidence -= 15;
  if (!input.farmingSystem) confidence -= 10;
  
  // Add some randomness
  confidence += Math.round((Math.random() * 10) - 5);
  
  // Ensure within 0-100 range
  return Math.max(0, Math.min(98, confidence));
}

function generateRecommendations(input: PredictionInput, yieldValue: number): string[] {
  const recommendations: string[] = [];
  
  // Crop-specific recommendations
  if (input.cropType) {
    if (input.nitrogen < 50) {
      recommendations.push(`Consider increasing nitrogen fertilization for better ${input.cropType} growth and yield potential.`);
    }
    
    if (input.phosphorus < 40) {
      recommendations.push(`Your soil appears low in phosphorus. Adding phosphate fertilizers could improve ${input.cropType} root development.`);
    }
    
    if (input.potassium < 40) {
      recommendations.push(`Increasing potassium levels may improve crop resilience and quality for your ${input.cropType}.`);
    }
  }
  
  // pH recommendations
  if (input.ph < 5.5) {
    recommendations.push("Your soil is acidic. Consider applying lime to raise the pH for better nutrient availability.");
  } else if (input.ph > 7.5) {
    recommendations.push("Your soil is alkaline. Adding organic matter or specific amendments could help lower the pH.");
  }
  
  // Water recommendations
  if (input.rainfall < 500) {
    recommendations.push("Your area has low rainfall. Consider implementing irrigation systems or water conservation practices.");
  } else if (input.rainfall > 1500) {
    recommendations.push("High rainfall in your area may lead to nutrient leaching. Consider split fertilizer applications.");
  }
  
  // Soil type recommendations
  if (input.soilType === 'sandy') {
    recommendations.push("Sandy soils have poor water retention. Adding organic matter can improve water holding capacity.");
  } else if (input.soilType === 'clay') {
    recommendations.push("Clay soils can have drainage issues. Consider raised beds or adding organic matter to improve structure.");
  }
  
  // Farming system recommendations
  if (input.farmingSystem === 'conventional' && yieldValue > baselineYields[input.cropType] * 0.8) {
    recommendations.push("Your conventional farming is performing well. Consider precision agriculture techniques to further optimize inputs.");
  } else if (input.farmingSystem === 'organic') {
    recommendations.push("In organic systems, crop rotation and cover crops are crucial for maintaining soil fertility and pest management.");
  }
  
  // Add general recommendation if few specific ones
  if (recommendations.length < 3) {
    recommendations.push("Regular soil testing is recommended to monitor nutrient levels and adjust your management practices accordingly.");
  }
  
  // Ensure we have at least 3 recommendations
  if (recommendations.length < 3) {
    recommendations.push("Maintaining good record-keeping of yields, inputs, and weather conditions can help identify patterns for future improvement.");
  }
  
  return recommendations;
}