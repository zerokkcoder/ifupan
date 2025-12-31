import { ref, watchEffect } from 'vue'

const isDark = ref(localStorage.getItem('theme') === 'dark' || 
  (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches))

export function useTheme() {
  /**
   * 切换主题模式 (亮色/暗色)
   */
  const toggleTheme = () => {
    // 添加过渡类，确保切换时有动画效果
    document.documentElement.classList.add('theme-transition')
    
    isDark.value = !isDark.value
    
    // 动画结束后移除过渡类
    setTimeout(() => {
      document.documentElement.classList.remove('theme-transition')
    }, 300)
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
