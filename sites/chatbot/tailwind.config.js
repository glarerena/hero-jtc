// sites/chatbot/tailwind.config.js
const bloomTheme = require('/Users/khalisahkhan/Documents/Flagship/Captsone/bloom/sites/public/tailwind.config.js'); // Adjust path based on your actual location of bloom-tailwind-config.js

module.exports = {
    content: [
      "./pages/**/*.{js,ts,jsx,tsx}",
      "./components/**/*.{js,ts,jsx,tsx}",
      "./sites/**/*.{js,ts,jsx,tsx}",
      // Add other directories containing JSX/TSX files
    ],
    theme: {
      extend: {
        colors: {
          primary: "#3490dc", // Example: customize colors
        },
        fontFamily: {
          sans: ['Arial', 'sans-serif'], // Example: add custom font
        },
      },
    },
    plugins: [],
  };
  