# Trading Analysis Bot

这是一个自动化交易分析工具，具备以下功能：

- 从 TradingView 获取各种时间周期的 K 线数据
- 使用 GPT-4 进行智能分析
- 生成易懂的市场分析报告
- 支持飞书通知功能

## 功能特性

- 实时获取 TradingView 的 K 线数据
- 支持多种交易品种（如股票、加密货币）
- 支持多种时间周期（如 15 分钟、1 小时、4 小时、日线）
- 使用 GPT-4 进行智能分析
- 分析内容包括：
  - 当前市场趋势判断
  - 关键支撑和阻力位
  - 技术指标分析
- 自动生成以日期命名的分析报告
- 支持飞书 Webhook 通知，每个时间周期单独推送

## 安装步骤

1. 创建并激活 Python 3.9 的虚拟环境：

   ```bash
   conda create -n trading_analysis python=3.9
   conda activate trading_analysis
   或
   python3.9 -m venv venv
   source venv/bin/activate
   ```

2. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

3. 配置 API 密钥：

   - 在 `config.py` 中设置您的 OpenAI API 密钥
   - 配置 TradingView 账号信息
   - 配置飞书 Webhook URL

4. 运行程序：

   ```bash
   python main.py
   ```

5. 运行程序：
   - 直接运行（前台运行）：
     ```bash
     python main.py
     ```
   - 部署为定时任务（后台运行）：
     ```bash
     chmod +x deploy.sh
     ./deploy.sh
     ```

## 配置说明

在 `config.py` 中可以设置以下参数：

- `OPENAI_API_KEY`: OpenAI API 密钥
- `TRADINGVIEW_USERNAME`: TradingView 用户名
- `TRADINGVIEW_PASSWORD`: TradingView 密码
- `SYMBOL`: 交易品种代码
- `TIMEFRAMES`: 需要分析的时间周期列表
- `GPT_MODEL`: 使用的 GPT 模型版本
- `FEISHU_WEBHOOK_URL`: 飞书 Webhook 地址
- `ANALYSIS_TIME`: 每日定时分析时间

## 输出说明

- 分析报告将保存在 `analysis_results` 目录下，文件名格式为 `market_analysis_YYYY-MM-DD.txt`
- 每个时间周期的分析结果会通过飞书机器人单独推送
- 分析内容包括市场趋势、支撑阻力位和技术指标分析

## 注意事项

- 请确保 API 密钥的安全性
- 建议使用虚拟环境运行程序
- 需要稳定的网络连接
- 建议将程序部署在服务器上运行

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License
