import React, { useContext } from 'react';
import { Sun, Moon, Sprout } from 'lucide-react';
import { ThemeContext } from '../../context/ThemeContext';

const Header: React.FC = () => {
  const { darkMode, toggleDarkMode } = useContext(ThemeContext);
  
  return (
    <header className="w-full py-4 px-6 shadow-md transition-colors duration-300 bg-white dark:bg-gray-800">
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        <div className="flex items-center space-x-2">
          <Sprout className="h-8 w-8 text-green-600 dark:text-green-400" />
          <h1 className="text-xl md:text-2xl font-bold text-gray-800 dark:text-white">
            CropYield<span className="text-green-600 dark:text-green-400">AI</span>
          </h1>
        </div>
        
        <button
          onClick={toggleDarkMode}
          className="p-2 rounded-full bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors duration-300"
          aria-label={darkMode ? "Switch to light mode" : "Switch to dark mode"}
        >
          {darkMode ? (
            <Sun className="h-5 w-5 text-yellow-500" />
          ) : (
            <Moon className="h-5 w-5 text-gray-600" />
          )}
        </button>
      </div>
    </header>
  );
};

export default Header;