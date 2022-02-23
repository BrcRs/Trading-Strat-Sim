from math import sin, cos, sqrt, log
from random import choice, random


"""We will use deap instead"""

class Symbolic():
    func_set = {
        "pow" : (2, lambda x, y : pow(x, y)),
        "+" : (2, lambda x, y : x + y),
        "-" : (2, lambda x, y : x - y),
        "*" : (2, lambda x, y : x * y),
        "1/" : (1, lambda x : 1./x),
        "sin" : (1, lambda x : sin(x)),
        "cos" : (1, lambda x : cos(x)),
        "sqrt" : (1, lambda x: sqrt(x)),
        "log" : (1, lambda x: log(x)),
    } 

    def __init__(self, input_size, output_size, maxsize=10):
        # variables
        # vnumber:cpt:h
        # v1:1:3

        # constant
        # c:cpt:h

        # Undefined
        # N:cpt:h

        # float
        # f:cpt:h
        # int
        # i:cpt:h

        self.input_variables = ["v"+str(i) for i in range(input_size)]
        self.output_size = output_size
        self.maxsize = maxsize
        self.tree = {}
        # cpt : int, current number of nodes
        cpt = 0
        ## init
        for i in range(self.output_size):
            f = choice(Symbolic.func_set.keys())
            arity = Symbolic.func_set[f][0]
            cpt += 1
            self.tree[f+":"+str(cpt)+":0"] = []
            ## Create undefined nodes
            for j in range(arity):
                cpt += 1
                self.tree[f].append("N:"+str(cpt)+":1")

        ## generation loop
        done = False
        while not done:
            done = True
            for k in self.tree.keys():
                for i in range(len(self.tree[k])):
                    v = self.tree[k][i]
                    if v.split(":")[0] == "N":
                        # chance to fuse with another node
                        if random() < 0.3:
                            # fuse
                            # find other none

                        # Variable, constant or function ?
                        if choice([True, False]) or len(self.tree.keys()) >= self.maxsize:
                            # Variable/constant
                            if choice([True, False]):
                                # variable
                                self.tree[choice(self.input_variables)]
                            else:
                                # constant
                        else:
                            # function


    def show(self):
        pass

def main():
    sym = Symbolic([4, 5, 5, 7], 3)

if __name__ == "__main__":
    main()