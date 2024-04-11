import sys
import time

from states import State

numbers = ''
open = []
visited = []

if len(sys.argv) > 1:
    numbers = list(sys.argv[1])

while len(numbers) != 9:
    numbers = list(input("Digite a sequência de 9 números correspondente ao estado do jogo: "))

open.append(State(numbers))
start_time = time.time()
while open != []:
    currentState = open.pop(0)
    if currentState.isSolution():
        end_time = time.time()
        currentState.evaluatePath()
        print('Nodos Visitados: %s' % len(visited))
        print("--- %s segundos ---" % (end_time - start_time))
        break
    children = currentState.generateChildren()
    for child in children:
        if child not in open and child not in visited:
            child.calculateCost()
            open.append(child)
        elif child in open: # if the child was reached by a shorter path then give the state on open the shorter path
            index = open.index(child)
            if child.pathLen < open[index].pathLen:
                open[index] = child
        else:  # if the child was reached by a shorter path then remove the state from closed add the child to open
            index = visited.index(child)
            if child.pathLen < visited[index].pathLen:
                visited.remove(visited[index])
                open.append(child)
            pass
    visited.append(currentState)
    open.sort(key=lambda x: x.cost)