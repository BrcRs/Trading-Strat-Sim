# from symbolic import Symbolic
from deap import PrimitiveSetTyped
import operator
import random
class Trader():
    nb_traders = 0
    horizon = 1
    def if_then_else(input, output1, output2):
        return output1 if input else output2
    # TODO determine a pset for each decision (buy/sell, vol, price)
    # TODO choose functions to add to pset
    # TODO think about types of functions and return
    # DONE solve buy/sell/donothing problem
    # because the output of the tree which decide wether or not to buy/sell/do nothing is of size 3. How can a mathematical expression return something with arity 3?
    # arity 2 is easy: negative: choice 1, positive: choice 2
    # ok when you think about it, we can define a zone around zero in which we do nothing
    # so output is float

    neutral_zone = 10

    # input is sell_price, sell_vol, buy_price, buy_vol, and open, close, high, low, vol=nb of transactions * h
    pset_buy = PrimitiveSetTyped("main", [float, int, float, int] + [float, float, float, float, int]*horizon, float)
    # pset_buy.addPrimitive(operator.xor, [bool, bool], bool)
    pset_buy.addPrimitive(operator.add, [float, float], float)
    pset_buy.addPrimitive(operator.sub, [float, float], float)
    pset_buy.addPrimitive(operator.mul, [float, float], float)
    pset_buy.addPrimitive(if_then_else, [bool, float, float], float)
    pset_buy.addPrimitive(operator.not_, [bool], bool)
    pset_buy.addPrimitive(operator.abs, [float], float)
    pset_buy.addPrimitive(operator.and_, [bool, bool], bool)
    pset_buy.addPrimitive(operator.floordiv, [float, float], float)
    pset_buy.addPrimitive(operator.neg, [float], float)
    pset_buy.addPrimitive(operator.or_, [bool, bool], bool)
    pset_buy.addPrimitive(operator.truediv, [float, float], float)
    pset_buy.addPrimitive(operator.xor, [bool, bool], bool)
    pset_buy.addPrimitive(operator.lt, [float, float], bool)
    pset_buy.addPrimitive(operator.le, [float, float], bool)
    pset_buy.addPrimitive(operator.eq, [float, float], bool)
    pset_buy.addPrimitive(operator.ne, [float, float], bool)
    pset_buy.addPrimitive(operator.ge, [float, float], bool)
    pset_buy.addPrimitive(operator.gt, [float, float], bool)

    pset_buy.addEphemeralConstant(lambda: random.random()*20 - 10, float)

    # pset_buy.addTerminal(3.0, float)
    # pset_buy.addTerminal(1, bool)

    # pset_buy.renameArguments(ARG0="sell_price")
    # pset_buy.renameArguments(ARG1="sell_vol") # TODO problem... we can't rename args without knowing how many we have

    def __init__(self, budget):
        Trader.nb_traders += 1
        self.name = "trader" + str(Trader.nb_traders)
        self.budget = budget
        ## randomize and generate symbolic genotype
        # gen_buy will decide wether to buy or sell or do nothing
        self.gen_buy = ??
        self.gen_vol = ??
        self.gen_price = ??

    def act(self, sell_price, sell_vol, buy_price, buy_vol, history):
        # input size : 4 + 5 * h with h the horizon
        # output : sell or buy, volume, price
        # outputsize : 3

        # what preprocessing?

        # Neural network?
        # Bayesian network?
        # decision tree?
        # symbolic regression? => let's go
        
        
        
        pass