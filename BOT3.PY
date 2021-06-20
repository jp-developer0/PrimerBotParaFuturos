from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
import config

client = RequestClient(api_key=config.API_KEY, secret_key=config.API_SECRET)

#client.change_margin_type(symbol = "BTCUSDT", marginType=FuturesMarginType.ISOLATED)
client.change_initial_leverage(symbol = "BTCUSDT", leverage=1)

result = client.post_order(
    symbol = 'BTCUSDT',
    side = OrderSide.BUY,
    orderType = OrderType.STOP_MARKET,
    stopPrice = 40000,
    closePosition=True,
    positionSide='SHORT'
)
