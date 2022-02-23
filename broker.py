# Traders send orders to the broker, basically buy or sell
# the broker gives informations to the traders such as current selling price, current buying price, open, close, high, low, volume
# the broker updates the price history, which is a list of open, close, high, low, vol=nb of transactions

class Broker():
    def __init__(self, price_init):
        # list of people and selling price
        # need to be able to find min sell value => ordered by price
        # get access to any seller
        # get number of same sellers (same price) => sum of all same
        # get desired number of stocks sold for each one
        self.selling = []
        # self.sell_vol = 0 # sell vol is length of self.selling
        self.buy_price = []
        # self.buy_vol = 0
        self.history = [[price_init]*4 + [0]]
        
    def info(self):
        # sell_price, sell_vol, buy_price, buy_vol, self.history
        return self.sell_price, self.sell_vol, self.buy_price, self.buy_vol, self.history