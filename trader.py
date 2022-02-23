class Trader():
    nb_traders = 0
    def __init__(self, budget):
        Trader.nb_traders += 1
        self.name = "trader" + str(Trader.nb_traders)
        self.budget = budget

    def act(self, sell_price, sell_vol, buy_price, buy_vol, history):
        pass