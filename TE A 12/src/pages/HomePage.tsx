import React from 'react';
import Layout from '../components/layout/Layout';
import Hero from '../components/home/Hero';
import PredictionForm from '../components/form/PredictionForm';
import InfoSection from '../components/home/InfoSection';

const HomePage: React.FC = () => {
  return (
    <Layout>
      <Hero />
      <div id="prediction-form" className="scroll-mt-16">
        <PredictionForm />
      </div>
      <InfoSection />
    </Layout>
  );
};

export default HomePage;