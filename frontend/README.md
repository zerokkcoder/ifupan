# Stock Fupan (AntMonitor Web)

基于 Vite + Vue 3 + TailwindCSS 的股票复盘/监控系统前端。
参考 [AntMonitor](https://gitee.com/antblack/ant-monitor) 的功能设计。

## 功能特性

- **市场概览 (Dashboard)**: 查看大盘指数、今日关注、市场情绪。
- **股票池 (Stock Pool)**: 管理自选股票，查看实时涨跌。
- **技术分析 (Analysis)**: 集成 ECharts，支持 K 线图展示。
- **系统设置 (Settings)**: 配置 Tushare Token、主题等。

## 技术栈

- Vue 3
- Vite
- TailwindCSS
- Vue Router
- ECharts
- Lucide Vue Next (图标库)

## 快速开始

### 安装依赖

```bash
npm install
```

### 启动开发服务器

```bash
npm run dev
```

### 构建生产版本

```bash
npm run build
```

## 目录结构

- `src/layouts`: 布局组件 (侧边栏、顶部导航)
- `src/views`: 页面视图 (Dashboard, StockList, Analysis, Settings)
- `src/router`: 路由配置
- `src/components`: 通用组件
