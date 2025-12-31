<template>
  <div class="flex h-screen bg-gray-50 dark:bg-dark-bg text-gray-900 dark:text-gray-100 font-sans transition-colors duration-300">
    <!-- Sidebar -->
    <aside 
      class="bg-white dark:bg-dark-card border-r border-gray-200 dark:border-dark-border flex flex-col transition-all duration-300 relative"
      :class="isCollapsed ? 'w-16' : 'w-38'"
    >
      <!-- Toggle Button -->
      <button 
        @click="toggleSidebar"
        class="absolute -right-3 top-6 bg-white dark:bg-dark-card border border-gray-200 dark:border-dark-border rounded-full p-1 text-gray-500 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-400 shadow-sm z-10"
      >
        <ChevronLeftIcon v-if="!isCollapsed" class="w-4 h-4" />
        <ChevronRightIcon v-else class="w-4 h-4" />
      </button>

      <div class="h-14 flex items-center px-4 border-b border-gray-100 dark:border-dark-border overflow-hidden">
        <div class="flex items-center gap-2">
            <!-- Logo -->
            <div class="w-8 h-8 bg-blue-600 rounded-lg flex-shrink-0 flex items-center justify-center text-white font-bold">i</div>
            <span 
              class="text-md font-bold text-gray-800 dark:text-white transition-opacity duration-200 whitespace-nowrap"
              :class="isCollapsed ? 'opacity-0 w-0' : 'opacity-100'"
            >
              iFupan
            </span>
        </div>
      </div>

      <nav class="flex-1 p-2 space-y-1 overflow-y-auto overflow-x-hidden custom-scrollbar">
        <router-link 
            v-for="item in navItems" 
            :key="item.path" 
            :to="item.path"
            class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
            active-class="bg-blue-50 dark:bg-blue-900/20 text-blue-600 dark:text-blue-400 font-medium"
            :title="isCollapsed ? item.name : ''"
        >
            <component :is="item.icon" class="w-5 h-5 flex-shrink-0" />
            <span 
              class="whitespace-nowrap transition-all duration-300"
              :class="isCollapsed ? 'opacity-0 w-0 hidden' : 'opacity-100'"
            >
              {{ item.name }}
            </span>
        </router-link>
      </nav>

      <div class="p-2 border-t border-gray-100 dark:border-dark-border overflow-hidden">
        <div class="flex items-center gap-3 px-2 py-2 text-gray-500 dark:text-gray-400">
            <div class="w-8 h-8 rounded-full bg-gray-200 dark:bg-gray-700 flex-shrink-0"></div>
            <div 
              class="flex flex-col transition-all duration-300"
              :class="isCollapsed ? 'opacity-0 w-0 hidden' : 'opacity-100'"
            >
                <span class="text-sm font-medium text-gray-700 dark:text-gray-200">User</span>
                <span class="text-xs">Free Plan</span>
            </div>
        </div>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 flex flex-col overflow-hidden">
        <!-- Header -->
        <header class="h-14 bg-white dark:bg-dark-card border-b border-gray-200 dark:border-dark-border flex items-center justify-between px-4 transition-colors duration-300">
            <h2 class="text-lg font-semibold text-gray-800 dark:text-white">{{ currentRouteName }}</h2>
            <div class="flex items-center gap-3">
                <button 
                  @click="toggleTheme" 
                  class="p-2 text-gray-500 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700 rounded-full transition-colors"
                  :title="isDark ? '切换亮色模式' : '切换暗色模式'"
                >
                    <SunIcon v-if="isDark" class="w-5 h-5" />
                    <MoonIcon v-else class="w-5 h-5" />
                </button>
                <button class="p-2 text-gray-500 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700 rounded-full transition-colors">
                    <BellIcon class="w-5 h-5" />
                </button>
            </div>
        </header>

        <!-- Page Content -->
        <div class="flex-1 overflow-y-auto bg-gray-50 dark:bg-dark-bg p-4 transition-colors duration-300">
            <router-view v-slot="{ Component }">
                <transition name="fade" mode="out-in">
                    <component :is="Component" />
                </transition>
            </router-view>
        </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { 
  LayoutDashboard, 
  ThumbsUp,
  List,
  LineChart,
  Compass,
  FileBarChart,
  History,
  Eye,
  Focus,
  PieChart,
  Network,
  Newspaper,
  FileText,
  Bot,
  Bell as BellIcon,
  ChevronLeft as ChevronLeftIcon,
  ChevronRight as ChevronRightIcon,
  Moon as MoonIcon,
  Sun as SunIcon
} from 'lucide-vue-next'
import { useTheme } from '../composables/useTheme'

const route = useRoute()
const { isDark, toggleTheme } = useTheme()
const isCollapsed = ref(false)

/**
 * 切换侧边栏的折叠状态
 */
const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value
}

const navItems = [
    { name: '市场概览', path: '/dashboard', icon: LayoutDashboard },
    { name: '个股推荐', path: '/recommendations', icon: ThumbsUp },
    { name: '股票列表', path: '/stocks', icon: List },
    { name: '个股走势', path: '/trend', icon: LineChart },
    { name: '股票发现', path: '/discovery', icon: Compass },
    { name: '策略报表', path: '/strategy-report', icon: FileBarChart },
    { name: '日志记录', path: '/logs', icon: History },
    { name: '专注监控', path: '/focus-monitor', icon: Eye },
    { name: '专注模式', path: '/focus-mode', icon: Focus },
    { name: '板块监控', path: '/sectors', icon: PieChart },
    { name: '板块关联', path: '/sector-relation', icon: Network },
    { name: '新闻资讯', path: '/news', icon: Newspaper },
    { name: '日报管理', path: '/daily-report', icon: FileText },
    { name: 'AI设置', path: '/ai-settings', icon: Bot },
]

const currentRouteName = computed(() => {
    const current = navItems.find(item => item.path === route.path)
    return current ? current.name : 'AntMonitor'
})
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Custom scrollbar for nav */
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: rgba(156, 163, 175, 0.5);
  border-radius: 20px;
}
</style>
