from tradingview_client import TradingViewClient
from gpt_analyzer import GPTAnalyzer
from config import SYMBOL, TIMEFRAMES, FEISHU_WEBHOOK_URL
from tqdm import tqdm
import time
from datetime import datetime
import os
from feishu_notifier import FeishuNotifier

def save_and_notify(analysis_results):
    """保存分析结果并发送飞书通知"""
    # 创建 analysis_results 目录（如果不存在）
    if not os.path.exists('analysis_results'):
        os.makedirs('analysis_results')
    
    # 生成文件名（使用当前日期）
    today = datetime.now().strftime('%Y-%m-%d')
    filename = f'analysis_results/market_analysis_{today}.txt'
    
    def clean_text(text):
        if text:
            # 去除 markdown 标记
            text = text.replace('#', '')
            text = text.replace('*', '')
            text = text.replace('### ', '')
            text = text.replace('#### ', '')
            # 确保段落之间有适当的空行
            text = text.replace('\n\n\n', '\n\n')
        return text
    
    # 初始化飞书通知器
    notifier = FeishuNotifier(FEISHU_WEBHOOK_URL)
    
    # 保存完整报告到文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"市场分析报告 - {today}\n")
        f.write(f"分析标的: {SYMBOL}\n")
        f.write("=" * 50 + "\n\n")
        
        # 对每个时间周期分别处理
        for timeframe, result in analysis_results.items():
            # 构建该时间周期的分析文本
            timeframe_text = f"分析时间: {today}\n"
            timeframe_text += f"分析标的: {SYMBOL}\n"
            timeframe_text += f"时间周期: {timeframe}\n"
            timeframe_text += "-" * 30 + "\n"
            timeframe_text += clean_text(result) if result else "分析失败"
            
            # 写入文件
            f.write(f"\n{timeframe} 时间周期分析\n")
            f.write("-" * 30 + "\n")
            f.write(clean_text(result) if result else "分析失败\n")
            f.write("\n" + "=" * 50 + "\n")
            
            # 发送单独的飞书通知
            notifier.send_analysis(SYMBOL, timeframe, timeframe_text)
            time.sleep(1)  # 添加短暂延迟，避免消息发送过于频繁
    
    print(f"\n分析报告已保存至: {filename}")

def analyze_timeframe(tv_client, gpt_analyzer, timeframe):
    """分析单个时间周期的数据"""
    print(f"\n开始分析 {SYMBOL} {timeframe} 时间周期数据...")
    
    # 创建获取数据的进度条
    with tqdm(total=2, desc=f"{timeframe} 分析进度", unit="step") as pbar:
        # 获取K线数据
        pbar.set_description(f"{timeframe} 获取数据")
        market_data = tv_client.get_klines(timeframe)
        if not market_data:
            return None
        pbar.update(1)
        
        # GPT分析
        pbar.set_description(f"{timeframe} GPT分析中")
        analysis = gpt_analyzer.analyze_market(market_data)
        pbar.update(1)
        
        return analysis

def main():
    # 初始化客户端
    tv_client = TradingViewClient(SYMBOL)
    gpt_analyzer = GPTAnalyzer()
    
    # 用于存储所有时间周期的分析结果
    analysis_results = {}
    
    # 分析每个时间周期
    for timeframe in TIMEFRAMES:
        analysis = analyze_timeframe(tv_client, gpt_analyzer, timeframe)
        analysis_results[timeframe] = analysis
        
        if analysis:
            print(f"{timeframe}周期分析完成")
        else:
            print(f"{timeframe}周期分析失败")
        
        # 避免API限制
        if timeframe != TIMEFRAMES[-1]:  # 如果不是最后一个时间周期
            time.sleep(2)
    
    # 保存分析结果
    save_and_notify(analysis_results)

if __name__ == "__main__":
    main() 