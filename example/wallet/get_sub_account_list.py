from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

sub_account_list = request_client.get_sub_account_list(email = None, status = None, page = None, limit = None)

print("======= Query Sub-account List(For Master Account) =======")
PrintMix.print_data(sub_account_list)
print("==========================================================")