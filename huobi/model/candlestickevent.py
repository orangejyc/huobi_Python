from huobi.model.constant import *
from huobi.model.candlestick import Candlestick


class CandlestickEvent:
    """
    The candlestick/kline data received by subscription of candlestick/kline.

    :member
        symbol: the symbol you subscribed.
        timestamp: the UNIX formatted timestamp generated by server in UTC.
        interval: candlestick/kline interval you subscribed.
        data: the data of candlestick/kline.

    """

    def __init__(self):
        self.symbol = ""
        self.timestamp = 0
        self.interval = CandlestickInterval.INVALID
        self.data = Candlestick()
