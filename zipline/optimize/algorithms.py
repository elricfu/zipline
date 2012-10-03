from logbook import Logger
from zipline.algorithm import TradingAlgorithm

logger = Logger('Algo')


class BuySellAlgorithm(TradingAlgorithm):
    """Algorithm that buys and sells alternatingly. The amount for
    each order can be specified. In addition, an offset that will
    quadratically reduce the amount that will be bought can be
    specified.

    This algorithm is used to test the parameter optimization
    framework. If combined with the UpDown trade source, an offset of
    0 will produce maximum returns.

    """

    def initialize(self, amount=100, offset=0):
        self.amount = amount
        self.buy_or_sell = -1
        self.offset = offset
        self.orders = []

    def handle_data(self, data):
        order_size = self.buy_or_sell * (self.amount - (self.offset ** 2))
        self.order(self.sids[0], order_size)
        logger.debug("ordering" + str(order_size))

        #sell next time around.
        self.buy_or_sell *= -1

        self.orders.append(order_size)
