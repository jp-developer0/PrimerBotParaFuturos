import config
from binance.client import Client
from binance.enums import *

client = Client(config.API_KEY, config.API_SECRET, tld='com')

futureBalance = client.futures_account_balance()
#print(futureBalance)

print("BNB ", futureBalance[0].get('balance') )
print("USDT ", futureBalance[1].get('balance') )
print("BUSD ", futureBalance[2].get('balance') )
