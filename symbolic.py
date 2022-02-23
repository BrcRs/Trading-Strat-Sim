from math import sin, cos, sqrt, log

class Symbolic():
    func_set = {
        "pow" : lambda x, y : pow(x, y),
        "+" : lambda x, y : x + y,
        "-" : lambda x, y : x - y,
        "*" : lambda x, y : x * y,
        "1/" : lambda x : 1./x,
        "sin" : lambda x : sin(x),
        "cos" : lambda x : cos(x),
        "sqrt" : lambda x: sqrt(x),
        "log" : lambda x: log(x),
    } 

    def __init__(self, input_variables, output_size, maxh=5):
        self.input_variables = input_variables
        self.output_size = output_size
        self.maxh = maxh


    def show(self):
        pass

def main():
    sym = Symbolic([4, 5, 5, 7], 3)

if __name__ == "__main__":
    main()