# 股票复盘系统 (iFupan)

一个综合性的股票市场分析和复盘系统，采用 Monorepo 结构组织。

## 🌟 功能特性

- **前端**：基于 Vue 3、Vite 和 TypeScript 构建，提供现代且响应迅速的用户界面。
- **后端**：由 FastAPI (Python) 驱动，提供高性能且易于开发的 API。
- **数据同步**：
  - 自动爬取 A 股股票列表及详情数据。
  - 支持高并发数据抓取。
  - 采用分布式爬虫设计思维。
- **后台更新**：集成 `DataUpdater` 模块，用于定时执行数据增量更新。
- **配置管理**：基于数据库的集中式配置存储，可通过 CLI 脚本进行管理。

## 📂 项目结构

- **`frontend/`**: Vue 3 应用程序源代码。
- **`backend/`**: Python FastAPI 应用程序源代码。
  - **`app/`**: 主要应用逻辑。
    - **`engines/`**: 数据同步引擎（例如 `StockSyncEngine`）。
    - **`core/`**: 核心模块（配置、日志、DataUpdater）。
    - **`models/`**: 数据库模型（Peewee ORM）。
  - **`scripts/`**: 实用脚本（例如配置管理器）。

## 🚀 快速开始

### 前端

1. 进入前端目录：
   ```bash
   cd frontend
   ```

2. 安装依赖：
   ```bash
   npm install
   ```

3. 启动开发服务器：
   ```bash
   npm run dev
   ```

### 后端

1. 进入后端目录：
   ```bash
   cd backend
   ```

2. 创建虚拟环境（推荐）：
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/macOS
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 启动开发服务器：
   ```bash
   uvicorn app.main:app --reload
   ```
   
   > **注意**：应用启动时会自动初始化数据库表。

## ⚙️ 配置管理

本系统使用基于数据库的配置系统 (`DataDictionary`)。你可以使用提供的脚本来管理配置。

### 使用方法

进入 `backend` 目录并运行：

```bash
# 设置或更新配置项
python scripts/manage_config.py set KEY VALUE --desc "描述信息"

# 列出所有配置项
python scripts/manage_config.py list
```

### 常用配置

| 键 (Key) | 值 (Value) | 描述 |
| :--- | :--- | :--- |
| `STOCK_SYNC_FORCE_UPDATE` | `0` 或 `1` | 设置为 `1` 可强制股票同步引擎更新所有股票详情，忽略最后更新日期。默认为 `0`。 |

## 🛠️ 技术栈

- **编程语言**: Python 3.8+, TypeScript
- **Web 框架**: FastAPI, Vue 3
- **数据库**: SQLite (默认) / MySQL (通过 Peewee 支持)
- **ORM**: Peewee
- **爬虫**: Requests, BeautifulSoup4
