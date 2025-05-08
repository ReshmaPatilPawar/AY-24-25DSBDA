import React from 'react';
import Layout from '../components/layout/Layout';
import PredictionResult from '../components/results/PredictionResult';

const ResultsPage: React.FC = () => {
  return (
    <Layout>
      <PredictionResult />
    </Layout>
  );
};

export default ResultsPage;