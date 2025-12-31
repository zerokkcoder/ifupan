import { ref, watchEffect } from 'vue'

const isDark = ref(localStorage.getItem('theme') === 'dark' || 
  (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches))

export function useTheme() {
  /**
   * 切换主题模式 (亮色/暗色)
   */
  const toggleTheme = () => {
    isDark.value = !isDark.value
  }

  watchEffect(() => {
    const html = document.documentElement
    if (isDark.value) {
      html.classList.add('dark')
      localStorage.setItem('theme', 'dark')
    } else {
      html.classList.remove('dark')
      localStorage.setItem('theme', 'light')
    }
  })

  return {
    isDark,
    toggleTheme
  }
}
