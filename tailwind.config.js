/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        darkBg: '#0B0B0B',
        charcoal: '#121212',
        glassBorder: 'rgba(255, 255, 255, 0.08)',
        glassBg: 'rgba(18, 18, 18, 0.6)',
        electricBlue: '#00D2FF',
        neonPurple: '#9D00FF',
        cyanGlow: '#00F0FF',
      },
      backgroundImage: {
        'glow-gradient': 'linear-gradient(135deg, #00D2FF 0%, #9D00FF 100%)',
        'indigo-gradient': 'linear-gradient(135deg, #00F0FF 0%, #3B82F6 50%, #4F46E5 100%)',
        'card-glow': 'radial-gradient(circle at top left, rgba(0, 210, 255, 0.15), transparent 70%)',
        'purple-glow': 'radial-gradient(circle at top right, rgba(157, 0, 255, 0.15), transparent 70%)',
      },
      animation: {
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'float': 'float 6s ease-in-out infinite',
        'glow': 'glow 3s ease-in-out infinite alternate',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        glow: {
          '0%': { boxShadow: '0 0 5px rgba(0, 210, 255, 0.2), 0 0 10px rgba(0, 210, 255, 0.1)' },
          '100%': { boxShadow: '0 0 15px rgba(157, 0, 255, 0.4), 0 0 25px rgba(157, 0, 255, 0.2)' },
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        outfit: ['Outfit', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
