module.exports = {
  content: [
    "./public/**/*.html",
    "./src/**/*.{html,js,vue}",
  ],
  darkMode:'class',
  theme: {
    extend: {
      fontFamily: {
        mono: ['LeferiBaseType-BoldA', 'LeferiBaseType-RegularA']
      }
    },
  },
  plugins: [],
}