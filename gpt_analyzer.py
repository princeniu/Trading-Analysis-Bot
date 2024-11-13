from openai import OpenAI
from config import OPENAI_API_KEY, GPT_MODEL

class GPTAnalyzer:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        
    def analyze_market(self, market_data):
        """使用GPT分析市场数据"""
        prompt = self._create_analysis_prompt(market_data)
        
        try:
            response = self.client.chat.completions.create(
                model=GPT_MODEL,
                messages=[
                    {"role": "system", "content": "你是一个专业的交易分析师，请基于提供的市场数据进行分析，并给出详细的市场分析报告。"},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"GPT分析错误: {e}")
            return None
            
    def _create_analysis_prompt(self, market_data):
        """创建分析提示词"""
        prompt = f"""
请分析以下市场数据并提供详细的分析报告：

价格数据：
- 当前价格：{int(market_data['close'])}
- 开盘价：{int(market_data['open'])}
- 最高价：{int(market_data['high'])}
- 最低价：{int(market_data['low'])}

技术指标：
- RSI：{int(market_data['technical_indicators']['rsi'])}
- MACD：{int(market_data['technical_indicators']['macd'])}
- MA20：{int(market_data['technical_indicators']['ma20'])}
- MA50：{int(market_data['technical_indicators']['ma50'])}

请提供：
1. 当前市场趋势判断
2. 关键支撑和阻力位
3. 技术指标分析
4. 潜在的交易机会

请直接给出分析内容，不要添加任何结论、建议或风险提示。
"""
        return prompt 