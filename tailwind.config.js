/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        wedding: {
          cream: '#FAF9F6',     // Light elegant background
          sage: '#4A5D4E',      // Sophisticated deep green
          rose: '#D3A297',      // Romantic dusty rose
          gold: '#C5A880',      // Premium golden accent
          charcoal: '#2D312E',  // Dark high-contrast reading text
          cardBg: 'rgba(250, 249, 246, 0.8)' // Translucent cream
        }
      },
      fontFamily: {
        serif: ['Taviraj', 'serif'],
        sans: ['Roboto', 'sans-serif'],
        script: ['"Dancing Script"', 'cursive']
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'float': 'float 6s ease-in-out infinite',
        'equalizer': 'equalizer 1.2s ease-in-out infinite alternate',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        equalizer: {
          '0%': { height: '4px' },
          '100%': { height: '24px' }
        }
      }
    },
  },
  plugins: [],
}
