
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
          primary: "#0077da", // Example: customize colors
        },
        fontFamily: {
          sans: ['Arial', 'sans-serif'], // Example: add custom font
        },
      },
    },
    plugins: [],
  };
  