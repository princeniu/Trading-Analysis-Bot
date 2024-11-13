import requests

class FeishuNotifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_analysis(self, symbol, timeframe, analysis_text):
        """发送单个时间周期的分析结果到飞书"""
        message = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": f"{symbol} {timeframe}周期市场分析报告",
                        "content": [
                            [
                                {
                                    "tag": "text",
                                    "text": analysis_text
                                }
                            ]
                        ]
                    }
                }
            }
        }

        try:
            response = requests.post(
                self.webhook_url,
                json=message,
                headers={'Content-Type': 'application/json'}
            )
            if response.status_code == 200:
                print(f"{symbol} {timeframe}周期分析通知发送成功")
            else:
                print(f"{symbol} {timeframe}周期分析通知发送失败: {response.text}")
        except Exception as e:
            print(f"发送{symbol} {timeframe}周期分析通知时出错: {e}") 