import React from 'react';

const HowItWorks: React.FC = () => {
  return (
    <section id="how-it-works" className="py-16 bg-gradient-to-b from-white to-gray-50">
      <div className="container mx-auto px-6">
        <h2 className="text-3xl font-bold text-center text-blue-900 mb-4">How It Works</h2>
        <p className="text-center text-gray-600 max-w-3xl mx-auto mb-12">
          Our SONAR classification system uses machine learning to identify underwater objects
        </p>
        
        <div className="relative">
          {/* Timeline line */}
          <div className="hidden md:block absolute left-1/2 transform -translate-x-1/2 h-full w-1 bg-blue-200"></div>
          
          {/* Steps */}
          <div className="space-y-12 md:space-y-0">
            {/* Step 1 */}
            <div className="relative flex flex-col md:flex-row items-center md:justify-between">
              <div className="flex md:w-5/12 md:justify-end mb-4 md:mb-0">
                <div className="bg-white p-5 rounded-lg shadow-md md:text-right max-w-md">
                  <h3 className="text-xl font-bold text-blue-900 mb-2">Data Collection</h3>
                  <p className="text-gray-600">
                    SONAR devices emit sound waves that bounce off underwater objects. The returned signals are captured as frequency data.
                  </p>
                </div>
              </div>
              
              <div className="z-10 bg-blue-900 text-white rounded-full h-10 w-10 flex items-center justify-center absolute md:relative md:left-auto md:transform-none left-1/2 transform -translate-x-1/2">1</div>
              
              <div className="md:w-5/12 md:pl-4 md:pt-0 pt-4">
                {/* Empty on right side for step 1 */}
              </div>
            </div>
            
            {/* Step 2 */}
            <div className="relative flex flex-col md:flex-row items-center md:justify-between">
              <div className="md:w-5/12 md:pr-4 mb-4 md:mb-0">
                {/* Empty on left side for step 2 */}
              </div>
              
              <div className="z-10 bg-blue-900 text-white rounded-full h-10 w-10 flex items-center justify-center absolute md:relative md:left-auto md:transform-none left-1/2 transform -translate-x-1/2">2</div>
              
              <div className="flex md:w-5/12 md:justify-start md:pl-4 md:pt-0 pt-4">
                <div className="bg-white p-5 rounded-lg shadow-md max-w-md">
                  <h3 className="text-xl font-bold text-blue-900 mb-2">Feature Extraction</h3>
                  <p className="text-gray-600">
                    The raw sonar data is processed into 60 frequency-domain features representing the energy within specific frequency bands.
                  </p>
                </div>
              </div>
            </div>
            
            {/* Step 3 */}
            <div className="relative flex flex-col md:flex-row items-center md:justify-between">
              <div className="flex md:w-5/12 md:justify-end mb-4 md:mb-0">
                <div className="bg-white p-5 rounded-lg shadow-md md:text-right max-w-md">
                  <h3 className="text-xl font-bold text-blue-900 mb-2">Machine Learning Model</h3>
                  <p className="text-gray-600">
                    A Logistic Regression model is trained on labeled examples of mines and rocks using their frequency patterns.
                  </p>
                </div>
              </div>
              
              <div className="z-10 bg-blue-900 text-white rounded-full h-10 w-10 flex items-center justify-center absolute md:relative md:left-auto md:transform-none left-1/2 transform -translate-x-1/2">3</div>
              
              <div className="md:w-5/12 md:pl-4 md:pt-0 pt-4">
                {/* Empty on right side for step 3 */}
              </div>
            </div>
            
            {/* Step 4 */}
            <div className="relative flex flex-col md:flex-row items-center md:justify-between">
              <div className="md:w-5/12 md:pr-4 mb-4 md:mb-0">
                {/* Empty on left side for step 4 */}
              </div>
              
              <div className="z-10 bg-blue-900 text-white rounded-full h-10 w-10 flex items-center justify-center absolute md:relative md:left-auto md:transform-none left-1/2 transform -translate-x-1/2">4</div>
              
              <div className="flex md:w-5/12 md:justify-start md:pl-4 md:pt-0 pt-4">
                <div className="bg-white p-5 rounded-lg shadow-md max-w-md">
                  <h3 className="text-xl font-bold text-blue-900 mb-2">Classification</h3>
                  <p className="text-gray-600">
                    New sonar readings are processed and fed to the model, which classifies them as either a mine (M) or a rock (R) with a confidence score.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HowItWorks;