// tailwind.config.js
module.exports = {
    content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'], // Adjust paths to match your file structure
    theme: {
      extend: {
        fontFamily: {
          'jakarta': ['"Plus Jakarta Sans"', 'sans-serif'], // Add Jakarta Sans
          'monospace-ui': ['"Monospace UI"', 'monospace'], // Add Monospace UI
        },
      },
    },
    plugins: [],
  };
  