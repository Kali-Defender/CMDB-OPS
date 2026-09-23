# CMDB + 自动化运维平台

> 面向中小型公司 IT 部门的服务器资产管理与批量运维平台。
>
> 解决「资产分散、登录信息靠口口相传、批量操作要一台台 SSH、操作无审计」的问题。

## 项目简介

以前用 Excel 记录 IP、账号、密码、用途，现在换成一个网站：

- 能登录
- 能看服务器列表
- 能增删改查
- 能批量执行命令
- 能留下执行记录

## 功能特性

### 主干功能（最小系统）

1. 登录
2. 服务器列表（支持搜索、分页）
3. 新增 / 修改 / 删除服务器
4. 批量执行命令（SSH）
5. 执行记录（审计）

### 规划中的加分功能

- 搜索分页、Excel 批量导入、角色权限、操作日志
- 定时巡检（APScheduler）、配置下发（Paramiko/SFTP）、邮件/钉钉通知
- 关系图谱（ECharts）、统计看板、插件系统

## 技术栈

| 技术 | 作用 |
| --- | --- |
| Python 3.11+ | 后端主语言 |
| FastAPI | Web 框架，提供前端调用的接口 |
| SQLAlchemy | ORM，用 Python 读写 MySQL |
| MySQL 8 | 存用户、服务器、执行记录 |
| JWT | 登录令牌 |
| Paramiko | SSH 连接目标服务器执行命令 |
| Vue 3 + Vite | 前端框架与构建工具 |
| Ant Design Vue | UI 组件库 |
| Axios | 前端调用后端接口 |
| APScheduler / ECharts | 加分项：定时巡检 / 图表看板 |

## 目录结构

```text
cmdb-ops/
├── backend/
│   ├── app/
│   │   ├── main.py              # 后端启动入口
│   │   ├── core/                # 配置、JWT、安全、数据库
│   │   ├── models/              # 数据库模型：用户、服务器、执行记录
│   │   ├── schemas/             # 请求和响应的数据结构
│   │   ├── api/                 # 接口路由：登录、资产、任务、记录
│   │   ├── services/            # 业务逻辑：资产、SSH 执行、日志
│   │   └── utils/               # 工具函数
│   ├── requirements.txt         # Python 依赖
│   └── .env.example             # 环境变量示例（真实 .env 不提交）
├── frontend/
│   ├── src/
│   │   ├── views/               # 页面：登录、服务器列表、执行记录
│   │   ├── components/          # 通用组件
│   │   ├── api/                 # 调后端接口
│   │   ├── router/              # 页面路由
│   │   └── store/               # 登录状态
│   ├── package.json
│   └── vite.config.js
├── docs/                        # 软著说明书、截图、操作手册
├── docker-compose.yml           # 后期一键启动
└── README.md
```

## 数据库设计

| 表 | 主要字段 |
| --- | --- |
| 服务器表 | 名称、IP、端口、登录账号、密码/密钥（加密）、类型、环境、负责人、状态、备注、创建时间 |
| 用户表 | 用户名、密码（加密）、姓名、角色、状态、创建时间 |
| 执行记录表 | 执行人、服务器、命令、结果、状态、执行时间 |

## 接口清单

| 编号 | 方法 | 路径 | 作用 | 是否需要登录 |
| --- | --- | --- | --- | --- |
| 1 | POST | /api/login | 登录，返回令牌 | 否 |
| 2 | GET | /api/servers | 获取服务器列表 | 是 |
| 3 | POST | /api/servers | 新增服务器 | 是 |
| 4 | PUT | /api/servers/{id} | 修改服务器 | 是 |
| 5 | DELETE | /api/servers/{id} | 删除服务器 | 是 |
| 6 | POST | /api/execute | 批量执行命令 | 是 |
| 7 | GET | /api/records | 获取执行记录 | 是 |
| 8 | GET | /api/users/me | 获取当前登录用户信息 | 是 |

## 页面清单

| 页面 | 路径 | 内容 |
| --- | --- | --- |
| 登录页 | /login | 用户名、密码、登录按钮 |
| 服务器列表页 | /servers | 搜索框、服务器表格、增删改、批量执行 |
| 执行记录页 | /records | 筛选条件、执行记录表格 |
| 布局框架 | 全局 | 顶部标题、左侧菜单、右侧内容区 |

## 快速开始

### 环境要求

- Python 3.11+（当前开发环境为 3.14，若依赖不兼容可回退 3.11/3.12）
- Node.js 18+
- MySQL 8

### 后端（当前已完成 Hello World）

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate    Linux/Mac: source .venv/bin/activate
pip install fastapi "uvicorn[standard]"
uvicorn app.main:app --reload
# 浏览器打开 http://127.0.0.1:8000
```

### 前端（待开发）

```bash
cd frontend
npm install
npm run dev
```

## 开发进度

- [x] 1. 搭建后端项目骨架，跑通 Hello World
- [ ] 2. 连接 MySQL，建三张表
- [ ] 3. 完成登录接口
- [ ] 4. 搭建前端项目骨架，跑通登录页
- [ ] 5. 前后端联调登录
- [ ] 6. 完成服务器列表接口 + 页面
- [ ] 7. 完成新增、修改、删除接口 + 页面
- [ ] 8. 完成批量执行命令接口 + 页面
- [ ] 9. 完成执行记录接口 + 页面
- [ ] 10. 整体联调、修 bug、整理软著材料

## 开发规范

- 每完成一个步骤并跑通后，提交代码并推送，提交信息以 `feat:` 开头
- `.env` 不提交（含数据库密码），只提交 `.env.example` 作为模板
