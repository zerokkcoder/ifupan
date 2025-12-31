import { createRouter, createWebHistory } from 'vue-router'
import MainLayout from '../layouts/MainLayout.vue'
import Dashboard from '../views/Dashboard.vue'
import Recommendations from '../views/Recommendations.vue'
import StockList from '../views/StockList.vue'
import StockTrend from '../views/StockTrend.vue'
import StockDiscovery from '../views/StockDiscovery.vue'
import StrategyReport from '../views/StrategyReport.vue'
import TradeLog from '../views/TradeLog.vue'
import FocusMonitor from '../views/FocusMonitor.vue'
import FocusMode from '../views/FocusMode.vue'
import SectorMonitor from '../views/SectorMonitor.vue'
import SectorRelation from '../views/SectorRelation.vue'
import News from '../views/News.vue'
import DailyReport from '../views/DailyReport.vue'
import AISettings from '../views/AISettings.vue'

const routes = [
  {
    path: '/',
    component: MainLayout,
    children: [
      { path: '', redirect: '/dashboard' },
      { path: 'dashboard', name: 'Dashboard', component: Dashboard },
      { path: 'recommendations', name: 'Recommendations', component: Recommendations },
      { path: 'stocks', name: 'StockList', component: StockList },
      { path: 'trend', name: 'StockTrend', component: StockTrend },
      { path: 'discovery', name: 'StockDiscovery', component: StockDiscovery },
      { path: 'strategy-report', name: 'StrategyReport', component: StrategyReport },
      { path: 'logs', name: 'TradeLog', component: TradeLog },
      { path: 'focus-monitor', name: 'FocusMonitor', component: FocusMonitor },
      { path: 'focus-mode', name: 'FocusMode', component: FocusMode },
      { path: 'sectors', name: 'SectorMonitor', component: SectorMonitor },
      { path: 'sector-relation', name: 'SectorRelation', component: SectorRelation },
      { path: 'news', name: 'News', component: News },
      { path: 'daily-report', name: 'DailyReport', component: DailyReport },
      { path: 'ai-settings', name: 'AISettings', component: AISettings },
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
