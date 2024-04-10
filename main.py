import sys

from states import State

numbers = ''
open = []
visited = []

if len(sys.argv) > 1:
    numbers = list(sys.argv[1])

while len(numbers) != 9:
    numbers = list(input("Digite a sequência de 9 números correspondente ao estado do jogo: "))

open.append(State(numbers))

while open != []:
    currentState = open.pop(0)
    if currentState.isSolution():
        print('solução') # TODO print path from start to current state
        break
    children = currentState.generateChildren()
    for child in children:
        if child not in open and child not in visited:
            child.calculateCost()
            open.append(child)
        elif child in open:
            pass # TODO if the child was reached by a shorter path then give the state on open the shorter path
        else:
            pass # TODO if the child was reached by a shorter path then remove the state from closed add the child to open
    visited.append(currentState)
    open.sort(key=lambda x: x.cost)