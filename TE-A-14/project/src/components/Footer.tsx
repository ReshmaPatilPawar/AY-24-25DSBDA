import React from 'react';
import { Github, Info } from 'lucide-react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-blue-950 text-white py-6 mt-20">
      <div className="container mx-auto px-6">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="mb-4 md:mb-0">
            <p className="text-gray-300 text-sm">
              &copy; {new Date().getFullYear()} SONAR Classifier
            </p>
          </div>
          <div className="flex space-x-4">
            <a 
              href="#" 
              className="text-gray-300 hover:text-teal-300 transition-colors flex items-center gap-1"
            >
              <Info className="h-4 w-4" />
              <span>Documentation</span>
            </a>
            <a 
              href="#" 
              className="text-gray-300 hover:text-teal-300 transition-colors flex items-center gap-1"
            >
              <Github className="h-4 w-4" />
              <span>GitHub</span>
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;