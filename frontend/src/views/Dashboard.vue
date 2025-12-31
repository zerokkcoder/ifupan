<template>
  <div class="p-4">
    <h1 class="text-xl font-bold mb-4 text-gray-900 dark:text-white">市场概览</h1>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <!-- 模拟卡片 -->
      <div class="bg-white dark:bg-dark-card p-4 rounded-lg shadow-sm border border-gray-100 dark:border-dark-border">
        <div class="text-gray-500 dark:text-gray-400 text-xs">上证指数</div>
        <div class="text-xl font-bold text-red-500 mt-1">3,050.23</div>
        <div class="text-xs text-red-500 mt-0.5">+1.2%</div>
      </div>
      <div class="bg-white dark:bg-dark-card p-4 rounded-lg shadow-sm border border-gray-100 dark:border-dark-border">
        <div class="text-gray-500 dark:text-gray-400 text-xs">深证成指</div>
        <div class="text-xl font-bold text-green-500 mt-1">9,850.11</div>
        <div class="text-xs text-green-500 mt-0.5">-0.5%</div>
      </div>
      <div class="bg-white dark:bg-dark-card p-4 rounded-lg shadow-sm border border-gray-100 dark:border-dark-border">
        <div class="text-gray-500 dark:text-gray-400 text-xs">创业板指</div>
        <div class="text-xl font-bold text-red-500 mt-1">1,950.88</div>
        <div class="text-xs text-red-500 mt-0.5">+0.8%</div>
      </div>
    </div>

    <div class="mt-4 grid grid-cols-1 lg:grid-cols-2 gap-4">
        <div class="bg-white dark:bg-dark-card p-4 rounded-lg shadow-sm border border-gray-100 dark:border-dark-border h-64">
            <h3 class="font-semibold text-gray-700 dark:text-gray-200 mb-3 text-sm">今日关注</h3>
            <div class="space-y-2">
                <div class="flex justify-between items-center border-b border-gray-100 dark:border-dark-border pb-2 text-sm">
                    <span class="text-gray-800 dark:text-gray-300">贵州茅台 (600519)</span>
                    <span class="text-red-500 font-medium">+1.5%</span>
                </div>
                <div class="flex justify-between items-center border-b border-gray-100 dark:border-dark-border pb-2 text-sm">
                    <span class="text-gray-800 dark:text-gray-300">宁德时代 (300750)</span>
                    <span class="text-green-500 font-medium">-0.8%</span>
                </div>
            </div>
        </div>
        <div class="bg-white dark:bg-dark-card p-4 rounded-lg shadow-sm border border-gray-100 dark:border-dark-border h-64">
            <h3 class="font-semibold text-gray-700 dark:text-gray-200 mb-3 text-sm">市场情绪</h3>
            <div class="flex items-center justify-center h-full pb-8">
                <span class="text-3xl font-bold text-orange-500">贪婪</span>
            </div>
        </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Dashboard logic here
</script>
