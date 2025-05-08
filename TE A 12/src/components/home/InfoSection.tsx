import React from 'react';
import { Cloud, Database, Server, Shield } from 'lucide-react';

const InfoSection: React.FC = () => {
  return (
    <div className="py-12 bg-green-50 dark:bg-gray-800 rounded-lg my-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="lg:text-center mb-16">
          <h2 className="text-base text-green-600 dark:text-green-400 font-semibold tracking-wide uppercase">How It Works</h2>
          <p className="mt-2 text-3xl leading-8 font-bold tracking-tight text-gray-900 dark:text-white sm:text-4xl">
            Smart Agriculture Meets Cloud Computing
          </p>
          <p className="mt-4 max-w-2xl text-xl text-gray-500 dark:text-gray-300 lg:mx-auto">
            Our advanced machine learning model runs on cloud infrastructure to provide accurate crop yield predictions with enterprise-grade reliability.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
          <div className="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-lg">
            <div className="flex items-center mb-4">
              <Database className="h-6 w-6 text-green-600 dark:text-green-400 mr-2" />
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Data Processing</h3>
            </div>
            <p className="text-gray-600 dark:text-gray-300">
              Process and analyze agricultural data using distributed computing for real-time insights and predictions.
            </p>
          </div>

          <div className="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-lg">
            <div className="flex items-center mb-4">
              <Cloud className="h-6 w-6 text-green-600 dark:text-green-400 mr-2" />
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Cloud Infrastructure</h3>
            </div>
            <p className="text-gray-600 dark:text-gray-300">
              Leveraging cloud services for scalable, reliable, and secure agricultural intelligence.
            </p>
          </div>

          <div className="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-lg">
            <div className="flex items-center mb-4">
              <Server className="h-6 w-6 text-green-600 dark:text-green-400 mr-2" />
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Edge Computing</h3>
            </div>
            <p className="text-gray-600 dark:text-gray-300">
              Process data closer to the source with edge devices for faster response times and reduced latency.
            </p>
          </div>

          <div className="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-lg">
            <div className="flex items-center mb-4">
              <Shield className="h-6 w-6 text-green-600 dark:text-green-400 mr-2" />
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Security & Compliance</h3>
            </div>
            <p className="text-gray-600 dark:text-gray-300">
              Enterprise-grade security with data encryption and compliance with agricultural data protection standards.
            </p>
          </div>
        </div>

        <div className="mt-10">
          <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-8 text-center">Cloud-Powered Prediction Pipeline</h3>
          <dl className="space-y-10 md:space-y-0 md:grid md:grid-cols-2 md:gap-x-8 md:gap-y-10">
            <div className="relative">
              <dt>
                <div className="absolute flex items-center justify-center h-12 w-12 rounded-md bg-green-500 dark:bg-green-600 text-white">
                  1
                </div>
                <p className="ml-16 text-lg leading-6 font-medium text-gray-900 dark:text-white">Data Collection</p>
              </dt>
              <dd className="mt-2 ml-16 text-base text-gray-500 dark:text-gray-300">
                Secure data ingestion from multiple sources including IoT sensors, weather stations, and manual input.
              </dd>
            </div>

            <div className="relative">
              <dt>
                <div className="absolute flex items-center justify-center h-12 w-12 rounded-md bg-green-500 dark:bg-green-600 text-white">
                  2
                </div>
                <p className="ml-16 text-lg leading-6 font-medium text-gray-900 dark:text-white">Cloud Processing</p>
              </dt>
              <dd className="mt-2 ml-16 text-base text-gray-500 dark:text-gray-300">
                Distributed processing using cloud computing resources for real-time analysis and prediction.
              </dd>
            </div>

            <div className="relative">
              <dt>
                <div className="absolute flex items-center justify-center h-12 w-12 rounded-md bg-green-500 dark:bg-green-600 text-white">
                  3
                </div>
                <p className="ml-16 text-lg leading-6 font-medium text-gray-900 dark:text-white">ML Model Training</p>
              </dt>
              <dd className="mt-2 ml-16 text-base text-gray-500 dark:text-gray-300">
                Continuous model training and optimization using distributed machine learning pipelines.
              </dd>
            </div>

            <div className="relative">
              <dt>
                <div className="absolute flex items-center justify-center h-12 w-12 rounded-md bg-green-500 dark:bg-green-600 text-white">
                  4
                </div>
                <p className="ml-16 text-lg leading-6 font-medium text-gray-900 dark:text-white">Results & Insights</p>
              </dt>
              <dd className="mt-2 ml-16 text-base text-gray-500 dark:text-gray-300">
                Secure delivery of predictions and insights through our cloud-based API infrastructure.
              </dd>
            </div>
          </dl>
        </div>

        <div className="mt-16 bg-white dark:bg-gray-700 p-8 rounded-lg shadow-lg">
          <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-6 text-center">Cloud Infrastructure Features</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="text-center">
              <p className="font-semibold text-gray-900 dark:text-white mb-2">Auto-Scaling</p>
              <p className="text-sm text-gray-600 dark:text-gray-300">Automatically adjusts computing resources based on demand</p>
            </div>
            <div className="text-center">
              <p className="font-semibold text-gray-900 dark:text-white mb-2">Global CDN</p>
              <p className="text-sm text-gray-600 dark:text-gray-300">Fast content delivery through distributed network</p>
            </div>
            <div className="text-center">
              <p className="font-semibold text-gray-900 dark:text-white mb-2">Disaster Recovery</p>
              <p className="text-sm text-gray-600 dark:text-gray-300">Automated backups and failover systems</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InfoSection;