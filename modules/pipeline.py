from modules.scraper import fetch_prices, fetch_news
from modules.sentiment import analyze_sentiment
from modules.indicators import add_indicators
from modules.backtester import run_backtest

def run_pipeline(symbol="AAPL", capital=100000):
    print("[BACKEND] Fetching price data...")
    prices_df = fetch_prices(symbol)

    print("[BACKEND] Fetching news...")
    news_df = fetch_news(symbol)

    print("[BACKEND] Running sentiment analysis...")
    sentiment_score = analyze_sentiment(news_df)

    print("[BACKEND] Adding indicators...")
    prices_df = add_indicators(prices_df)

    print("[BACKEND] Running backtest...")
    results = run_backtest(prices_df, sentiment_score, capital)

    return results
