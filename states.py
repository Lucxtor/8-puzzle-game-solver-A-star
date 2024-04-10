class State():
    def __init__(self, position, parent=None):
        self.state = position
        self.cost = 0
        self.parent = parent

    def isSolution(self):
        if self.state == ['1', '2', '3', '5', '4', '6', '7', '8', '0']:
            return True
        return False

    def calculateCost(self):
        self.cost += 1 # TODO apply heuristic

    def generateChildren(self):
        pass # TODO generate based on possible moves and return a list of States with current state as parent