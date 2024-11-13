#!/bin/bash

# 安装依赖
pip install -r requirements.txt

# 启动定时任务
nohup python scheduler.py > trading_bot.log 2>&1 &

echo "Trading Analysis Bot 已启动" 