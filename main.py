import requests
url = f"https://query1.finance.yahoo.com/v8/finance/chart/MSFT"
print(requests.get(url))