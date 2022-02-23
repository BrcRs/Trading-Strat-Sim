
from broker import Broker
from trader import Trader

def main():
    INITPRICE = 10.
    INITBUDGET = 2000
    NBAGENTS = 5000
    ITE = 365 * 5 # 5 years, daily
    # init broker
    broker = Broker(INITPRICE)
    # init NBagents agents
    agents = [Trader(INITBUDGET) for _ in range(NBAGENTS)]
    agents = {t.name : t for t in agents}
    for i in range(ITE):
        # randomize order ? not necessary
        for name in agents.keys():
            agent = agents[name]
            # each trader gets the info
            # each trader chooses and submits an action (buy or sell)
            # the order should specify the type, the volume and the value
            order = agent.act(*broker.info())
        # at the end of iteration, remove people with negative budget (rerandomize)
        # for name in agents.keys():
            # if agents[name].budget <= 0:
        # show best agents
        # show stats
        # show stock history
        # broker increments period
        broker.next()


if __name__ == "__main__":
    main()