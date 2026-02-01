📈 Trading Bot with Sentiment Analysis

An end-to-end AI-powered trading assistant built using Python + Streamlit that combines technical indicators, news sentiment analysis, strategy logic, and backtesting to help traders make informed decisions.

🚀 Features

🔴 Live Trading Signals

1.Real-time trading signals based on technical indicators
2.Strategy-driven BUY / SELL / HOLD recommendations

📰 News & Sentiment Analysis

1.Scrapes financial news headlines
2.Applies sentiment analysis to gauge market mood
3.Helps avoid trades during negative sentiment phases

🧪 Strategy Backtesting

1.Test trading strategies on historical data
2.Evaluate performance before deploying live
3.Generates metrics like:
    Total returns
    Win/Loss ratio
    Drawdowns

⚙️ Custom Strategy Settings

Adjustable parameters (indicators, thresholds, logic)
Experiment with different strategies easily

📊 Interactive Dashboard

1.Built with Streamlit
2.Multiple pages for clean navigation
3.Visual insights for better decision-making

🗂️ Project Structure
trading-bot-streamlit/
│
├── app.py                  # Main Streamlit entry point
├── requirements.txt        # Project dependencies
│
├── assets/
│   ├── banner.png          # UI banner
│   └── logo.png            # App logo
│
├── modules/
│   ├── scraper.py          # News scraping logic
│   ├── sentiment.py        # Sentiment analysis module
│   ├── indicators.py       # Technical indicators (RSI, MACD, etc.)
│   ├── strategy.py         # Trading strategy logic
│   └── backtester.py       # Strategy backtesting engine
│
├── pages/
│   ├── Live_Signals.py     # Live trading signals UI
│   ├── News_And_Sentiment.py # News & sentiment dashboard
│   ├── Strategy_Settings.py  # Strategy configuration page
│   └── Backtest.py         # Backtesting interface

🧠 Tech Stack

1.Python
2.Streamlit – Interactive web dashboard
3.Pandas / NumPy – Data handling
4.Technical Analysis – RSI, MACD, Moving Averages
5.NLP – News sentiment analysis
6.Web Scraping – Financial news extraction

⚙️ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/Amank0704/Trading-Bot-with-Sentiment-Analysis
cd Trading-Bot-with-Sentiment-Analysis

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py


📌 Use Cases

1.Retail traders looking for signal confirmation
2.Learning algorithmic trading concepts
3.Practicing:
    Technical Analysis
    Strategy design
    Backtesting
    Sentiment-based filtering
4.Portfolio project for FinTech / ML / Data roles

🧪 Example Workflow
1.Configure strategy parameters
2.Check News Sentiment
3.View Live Trading Signals
4.Run Backtesting
5.Improve strategy based on results

🔮 Future Improvements:
✅ WebSocket-based live price streaming
✅ Broker API integration (paper trading)
✅ ML-based signal prediction
✅ React frontend + FastAPI backend
✅ Strategy optimization with Optuna

👨‍💻 Author

Aman Kshirsagar
B.Tech – AI & Data Science
Focused on Machine Learning, FinTech & Backend Systems

⭐ If you like this project
Give it a ⭐ on GitHub — it really helps!