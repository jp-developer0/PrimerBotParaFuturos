import config
from binance.client import Client
from binance.enums import *

client = Client(config.API_KEY, config.API_SECRET, tld='com')

tickers = client.get_all_tickers()
maxPrecio = 0
maxMoneda = ''
minPrecio = 999999
minMoneda = ''


for tick in tickers:
    if tick['symbol'][-4:] != 'USDT' and tick['symbol'][-4:] != 'BUSD' and tick['symbol'][-3:] != 'BNB':
        continue
    klines = client.get_historical_klines(tick['symbol'], Client.KLINE_INTERVAL_5MINUTE, "5 minute ago UTC")
    if len(klines) != 1:
        continue

    variation = float(klines[0][4]) * 100 /  float(klines[0][1])

    if maxPrecio < variation:
        maxPrecio = variation
        maxMoneda = tick['symbol']

    if minPrecio > variation:
        minPrecio = variation
        minMoneda = tick['symbol']

    print("MAYOR " , maxMoneda ,  " " , maxPrecio)
    print("MENOR " , minMoneda ,  " " , minPrecio)
    print("--------------------")
