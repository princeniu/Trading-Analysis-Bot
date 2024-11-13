import schedule
import time
from datetime import datetime
from main import main
from config import ANALYSIS_TIME

def job():
    print(f"开始执行定时分析任务 - {datetime.now()}")
    try:
        main()
    except Exception as e:
        print(f"执行任务时出错: {e}")

def run_scheduler():
    # 设置每日定时任务
    schedule.every().day.at(ANALYSIS_TIME).do(job)
    
    print(f"定时任务已启动，将在每天 {ANALYSIS_TIME} 执行分析")
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    run_scheduler() 