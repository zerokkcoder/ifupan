<template>
  <div class="p-4">
    <div class="flex justify-between items-center mb-4">
        <h1 class="text-xl font-bold text-gray-900 dark:text-white">股票池</h1>
        <button class="bg-blue-600 text-white px-3 py-1.5 text-sm rounded hover:bg-blue-700 transition shadow-sm">添加股票</button>
    </div>
    
    <div class="bg-white dark:bg-dark-card rounded-lg shadow-sm border border-gray-100 dark:border-dark-border overflow-hidden">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200 dark:divide-dark-border">
          <thead class="bg-gray-50 dark:bg-gray-800/50">
            <tr>
              <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">代码</th>
              <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">名称</th>
              <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">现价</th>
              <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">涨跌幅</th>
              <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">行业</th>
            </tr>
          </thead>
          <tbody class="bg-white dark:bg-dark-card divide-y divide-gray-200 dark:divide-dark-border">
            <tr v-for="stock in stocks" :key="stock.code" class="hover:bg-gray-50 dark:hover:bg-gray-800/50 transition-colors">
              <td class="px-4 py-3 whitespace-nowrap text-sm font-medium text-gray-900 dark:text-gray-200">{{ stock.code }}</td>
              <td class="px-4 py-3 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">{{ stock.name }}</td>
              <td class="px-4 py-3 whitespace-nowrap text-sm text-gray-900 dark:text-gray-200">{{ stock.price }}</td>
              <td class="px-4 py-3 whitespace-nowrap text-sm font-medium" :class="stock.change > 0 ? 'text-red-500' : 'text-green-500'">
                  {{ stock.change > 0 ? '+' : '' }}{{ stock.change }}%
              </td>
              <td class="px-4 py-3 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">{{ stock.industry }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const stocks = ref([
    { code: '600519', name: '贵州茅台', price: 1750.00, change: 1.2, industry: '白酒' },
    { code: '300750', name: '宁德时代', price: 180.50, change: -0.5, industry: '电池' },
    { code: '000858', name: '五粮液', price: 145.20, change: 0.8, industry: '白酒' },
    { code: '601318', name: '中国平安', price: 45.30, change: -0.2, industry: '保险' },
    { code: '002594', name: '比亚迪', price: 210.00, change: 2.1, industry: '汽车' },
])
</script>
