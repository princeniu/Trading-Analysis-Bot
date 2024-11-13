from tradingview_ta import TA_Handler
import pandas as pd

class TradingViewClient:
    def __init__(self, symbol, exchange="BINANCE"):
        self.symbol = symbol
        self.exchange = exchange
        
    def get_klines(self, interval):
        """获取K线数据"""
        handler = TA_Handler(
            symbol=self.symbol,
            exchange=self.exchange,
            screener="crypto",
            interval=interval
        )
        
        try:
            analysis = handler.get_analysis()
            return {
                "close": analysis.indicators["close"],
                "open": analysis.indicators["open"],
                "high": analysis.indicators["high"],
                "low": analysis.indicators["low"],
                "volume": analysis.indicators["volume"],
                "technical_indicators": {
                    "rsi": analysis.indicators["RSI"],
                    "macd": analysis.indicators["MACD.macd"],
                    "ma20": analysis.indicators["SMA20"],
                    "ma50": analysis.indicators["SMA50"]
                }
            }
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None 