from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *
from binance.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
tranId = request_client.post_margin_transfer(asset="BTC", amount=0.001, transferType=MarginTransferType.IN)
print("Transaction Id: ", tranId)
