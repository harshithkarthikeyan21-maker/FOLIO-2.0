import requests
import json

def return_live_prices(ticker):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=header)
        
        if response.status_code != 200:
            print(f"LIVE PRICE WARNING: Status {response.status_code} for {ticker}")
            return None
            
        r = response.json()
        
        if not r.get("chart", {}).get("result"):
            return None
            
        meta = r["chart"]["result"][0]["meta"]
        price = meta.get("regularMarketPrice")
        prev_close = meta.get("chartPreviousClose")
        
        if price is None or prev_close is None:
            return None
            
        change = price - prev_close
        percent_change = (change / prev_close) * 100

        return {
            "ticker": ticker,
            "price": f"{price:,.2f}",
            "change": f"{change:+,.2f}",
            "percent_change": f"({percent_change:+.2f}%)",
            "raw_price": float(price),
        }
    
    except Exception as e:
        print(f"CRITICAL ERROR FETCHING LIVE PRICE FOR {ticker}: {e}")
        return None
