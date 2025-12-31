/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // 参考 AntMonitor/Fluent Design 可能需要的颜色
        primary: '#0078d4', // 示例 Fluent Blue
        dark: {
            bg: '#1e1e1e',
            card: '#252526',
            border: '#3e3e42'
        }
      }
    },
  },
  plugins: [],
}
