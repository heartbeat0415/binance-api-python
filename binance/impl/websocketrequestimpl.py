import time
from binance.impl.websocketrequest import WebsocketRequest
from binance.impl.utils.channels import *
from binance.impl.utils.channelparser import ChannelParser
from binance.impl.utils.timeservice import *
from binance.impl.utils.inputchecker import *
from binance.model import *
# from binance.model.candlestickrequest import CandlestickRequest
# For develop
from binance.base.printobject import *


class WebsocketRequestImpl(object):

    def __init__(self, api_key):
        self.__api_key = api_key

    def subscribe_candlestick_event(self, symbol, interval, callback, error_handler=None):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(interval, "interval")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(kline_channel(symbol, interval))
            time.sleep(0.01)

        def json_parse(json_wrapper):
            candle_stick_event_obj = CandlestickEvent.json_parse(json_wrapper)
            return candle_stick_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request

    def subscribe_aggregate_trade_event(self, symbol, callback, error_handler=None):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(aggregate_trade_channel(symbol))
            time.sleep(0.01)

        def json_parse(json_wrapper):
            aggregate_trade_event_obj = AggregateTradeEvent.json_parse(json_wrapper)
            return aggregate_trade_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request

    def subscribe_trade_event(self, symbol, callback, error_handler=None):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(trade_channel(symbol))
            time.sleep(0.01)

        def json_parse(json_wrapper):
            trade_event_obj = TradeEvent.json_parse(json_wrapper)
            return trade_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request

    def subscribe_symbol_miniticker_event(self, symbol, callback, error_handler=None):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(symbol_miniticker_channel(symbol))
            time.sleep(0.01)

        def json_parse(json_wrapper):
            symbol_miniticker_event_obj = SymbolMiniTickerEvent.json_parse(json_wrapper)
            return symbol_miniticker_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request

    def subscribe_all_miniticker_event(self, callback, error_handler=None):
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(all_miniticker_channel())
            time.sleep(0.01)

        def json_parse(json_wrapper):
            all_miniticker_event_obj = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                mini_ticker_event_obj = SymbolMiniTickerEvent.json_parse(item)
            all_miniticker_event_obj.append(mini_ticker_event_obj)
            return all_miniticker_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request
    
    def subscribe_symbol_ticker_event(self, symbol, callback, error_handler=None):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(symbol_ticker_channel(symbol))
            time.sleep(0.01)

        def json_parse(json_wrapper):
            symbol_ticker_event_obj = SymbolTickerEvent.json_parse(json_wrapper)
            return symbol_ticker_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request
    
    def subscribe_all_ticker_event(self, callback, error_handler=None):
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(all_ticker_channel())
            time.sleep(0.01)

        def json_parse(json_wrapper):
            all_ticker_event_obj = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                ticker_event_obj = SymbolTickerEvent.json_parse(item)
            all_ticker_event_obj.append(ticker_event_obj)
            return all_ticker_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request
      
    def subscribe_symbol_bookticker_event(self, symbol, callback, error_handler=None):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(symbol_bookticker_channel(symbol))
            time.sleep(0.01)

        def json_parse(json_wrapper):
            symbol_bookticker_event_obj = SymbolBookTickerEvent.json_parse(json_wrapper)
            return symbol_bookticker_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request
    
    def subscribe_all_bookticker_event(self, callback, error_handler=None):
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(all_bookticker_channel())
            time.sleep(0.01)

        def json_parse(json_wrapper):
            all_bookticker_event_obj = SymbolBookTickerEvent.json_parse(json_wrapper)
            return all_bookticker_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request
  
    def subscribe_book_depth_event(self, symbol, limit, callback, error_handler=None):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(limit, "limit")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(book_depth_channel(symbol, limit))
            time.sleep(0.01)

        def json_parse(json_wrapper):
            book_depth_event_obj = OrderBook.json_parse(json_wrapper)
            return book_depth_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request
  
    def subscribe_diff_depth_event(self, symbol, callback, error_handler=None):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(diff_depth_channel(symbol))
            time.sleep(0.01)

        def json_parse(json_wrapper):
            diff_depth_event_obj = DiffDepthEvent.json_parse(json_wrapper)
            return diff_depth_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request
  
    def subscribe_user_data_event(self, listenKey, callback, error_handler=None):
        check_should_not_none(listenKey, "listenKey")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(user_data_channel(listenKey))
            time.sleep(0.01)

        def json_parse(json_wrapper):
            print("event type: ", json_wrapper.get_string("e"))
            print(json_wrapper)
            if(json_wrapper.get_string("e") == "outboundAccountInfo"):
                result = OutboundAccountInfo.json_parse(json_wrapper)
            elif(json_wrapper.get_string("e") == "outboundAccountPosition"):
                result = OutboundAccountPosition.json_parse(json_wrapper)
            elif(json_wrapper.get_string("e") == "balanceUpdate"):
                result = BalanceUpdate.json_parse(json_wrapper)
            elif(json_wrapper.get_string("e") == "executionReport"):
                print(json_wrapper)
                result = ExecutionReport.json_parse(json_wrapper)
            elif(json_wrapper.get_string("e") == "listStatus"):
                result = ListStatus.json_parse(json_wrapper)
            return result

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request