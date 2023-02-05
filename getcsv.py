import csv
from requests import get

url = "https://api.binance.com/api/v3/klines?symbol=BNBUSDT&interval=1m&limit=1000"

file = "bnb.csv"

header = ['TIME_OPEN', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'TIME_CLOSE', 'QUOTE', 'TRADES', 'BUY_BASE_ASSET',
          'BUY_QUOTE_ASSET', 'IGNORE']

with open(file, "w") as fp:
    writer = csv.writer(fp)
    writer.writerow(header)
    data = get(url).json()
    writer.writerows(data)
    fp.close()
