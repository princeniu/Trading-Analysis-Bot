# Trading Analysis Bot

这是一个自动化交易分析工具，能够：

- 从 TradingView 获取各种时间周期的 K 线数据
- 使用 GPT-4 进行智能分析
- 生成易懂的市场分析报告

## 功能特性

- 从 TradingView 获取实时 K 线数据
- 支持多个交易品种（股票、加密货币等）
- 支持多个时间周期（15 分钟、1 小时、4 小时、日线等）
- 使用 GPT-4 进行智能分析
- 分析内容包括：趋势判断、支撑阻力位、技术指标解读、潜在风险提示等
- 自动生成日期命名的分析报告

## 安装步骤

# 创建名为 trading_analysis 的新环境，使用 Python 3.9

conda create -n trading_analysis python=3.9

# 激活环境

conda activate trading_analysis

1. 安装依赖：
   pip install -r requirements.txt
2. 配置 API 密钥：

- 在 config.py 中设置您的 OpenAI API 密钥
- 配置 TradingView 账号信息

3. 运行程序：
   python main.py

## 配置说明

在 `config.py` 中可以设置：

- OPENAI_API_KEY: OpenAI API 密钥
- TRADINGVIEW_USERNAME: TradingView 用户名
- TRADINGVIEW_PASSWORD: TradingView 密码
- SYMBOL: 交易品种代码
- TIMEFRAMES: 需要分析的时间周期列表
- GPT_MODEL: 使用的 GPT 模型版本

## 输出示例

分析报告将保存在 `analysis_results` 目录下，文件名格式为 `market_analysis_YYYY-MM-DD.txt`。

## 注意事项

- 请确保 API 密钥的安全性
- 建议使用虚拟环境运行程序
- 需要稳定的网络连接

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License
