import React from 'react';
import { BinaryIcon as Sonar } from 'lucide-react';

const Header: React.FC = () => {
  return (
    <header className="bg-gradient-to-r from-blue-950 to-blue-900 text-white py-4 px-6 shadow-md">
      <div className="container mx-auto flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <Sonar className="h-8 w-8 text-teal-400" />
          <h1 className="text-2xl font-bold tracking-tight">SONAR Classifier</h1>
        </div>
        <nav>
          <ul className="flex space-x-6">
            <li>
              <a href="#" className="text-teal-300 hover:text-white transition-colors">Home</a>
            </li>
            <li>
              <a href="#about" className="text-gray-300 hover:text-white transition-colors">About</a>
            </li>
            <li>
              <a href="#how-it-works" className="text-gray-300 hover:text-white transition-colors">How It Works</a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;