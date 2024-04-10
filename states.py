class State():
    def __init__(self, position, parent=None):
        self.state = position
        self.cost = 0
        self.parent = parent

    def __str__(self):
        state_str = '\n'.join([str(self.state[i:i+3]) for i in range(0, 9, 3)])
        return f"Estado:\n{state_str}\nCusto: {self.cost}"

    def isSolution(self):
        if self.state == ['1', '2', '3', '4', '5', '6', '7', '8', '0']:
            return True
        return False

    def calculateCost(self):
        self.cost += 1 # TODO apply heuristic

    def generateChildren(self):

            # Index do tabuleiro
            # 0 1 2
            # 3 4 5
            # 6 7 8

            # Se index 0 direita ou baixo
            # Se index 1 direita, esquerda ou baixo
            # Se index 2 esquerda ou baixo
            # Se index 3 cima, direita ou baixo
            # Se index 4 cima, direita, esquerda ou baixo
            # Se index 5 cima, esquerda ou baixo 
            # Se Index 6 cima ou direita 
            # Se index 7 cima, direita ou esquerda
            # Se index 8 cima ou esquerda
        
            # Direita = index + 1
            # Esquerda = index - 1
            # Cima = index - 3
            # Baixo = index + 3

        index = self.state.index('0')
        children = []
        aux = ''

        if index not in [2, 5, 8]: # Movimento para a direita
            stateCopy = self.state.copy()
            aux = stateCopy[index+1]
            stateCopy[index+1] = '0'
            stateCopy[index] = aux

            children.append(State(stateCopy, self))
        
        if index not in [0, 3, 6]: # Movimento para a esquerda
            stateCopy = self.state.copy()
            aux = stateCopy[index-1]
            stateCopy[index-1] = '0'
            stateCopy[index] = aux

            children.append(State(stateCopy, self))

        if index not in [6, 7, 8]: # Movimento para baixo
            stateCopy = self.state.copy()
            aux = stateCopy[index+3]
            stateCopy[index+3] = '0'
            stateCopy[index] = aux

            children.append(State(stateCopy, self))
        
        if index not in [0, 1, 2]: # Movimento para cima
            stateCopy = self.state.copy()
            aux = stateCopy[index-3]
            stateCopy[index-3] = '0'
            stateCopy[index] = aux

            children.append(State(stateCopy, self))

        return children