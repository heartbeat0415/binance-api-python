from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *
from binance.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.cancel_margin_order(symbol="BTCUSDT", orderId=28)
PrintBasic.print_obj(result)
