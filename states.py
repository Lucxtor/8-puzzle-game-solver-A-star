class State():
    def __init__(self, position, parent=None, move='', pathLen=0):
        self.state = position
        self.cost = 0
        self.parent = parent
        self.move = move
        self.pathLen = pathLen

    def __eq__(self, state):
        return self.state == state

    def __str__(self):
        state_str = '\n'.join([str(self.state[i:i+3]) for i in range(0, 9, 3)])
        return f"{self.move}\nNovo estado:\n{state_str}\nCusto: {self.cost}\n"

    def isSolution(self):
        if self.state == ['1', '2', '3', '4', '5', '6', '7', '8', '0']:
            return True
        return False

    def calculateCost(self):

        # Custo Uniforme
        # self.cost = self.pathLen 

        # Heuristica Simples
        # self.cost = self.pathLen
        # for index, value in enumerate(self.state):
        #     if int(value)-1 != index and int(value) != 0:
        #         self.cost += 1

        # Heuristica Otimizada
        # self.cost = self.pathLen
        # for index, value in enumerate(self.state):
        #     valueRightIndex = int(value)-1
        #     if valueRightIndex != index and int(value) != 0:
        #         line = index // 3 
        #         valueRightLine = valueRightIndex // 3
        #         lineError = abs(line - valueRightLine)
        #         column = index % 3
        #         valueRightColumn = valueRightIndex % 3
        #         columnError = abs(column - valueRightColumn)
        #         self.cost += (lineError + columnError) 

        # Heuristica Otimizada + custo diretamente inverso
        self.cost = self.pathLen
        for index, value in enumerate(self.state):
            valueRightIndex = int(value)-1
            if valueRightIndex != index and int(value) != 0:
                # Distancia até o local correto
                line = index // 3 
                valueRightLine = valueRightIndex // 3
                lineError = abs(line - valueRightLine)
                column = index % 3
                valueRightColumn = valueRightIndex % 3
                columnError = abs(column - valueRightColumn)
                self.cost += (lineError + columnError) 
                # Diretamente invertida
                if index % 3 != 2:
                    if (int(self.state[index+1]) == int(self.state[index])-1):
                        self.cost += 5
                elif index // 3 != 2:
                    if (int(self.state[index+3]) == int(self.state[index])-3):
                        self.cost += 5

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

            children.append(State(stateCopy, self, 'Move ' + aux + ' para a esquerda', self.pathLen+1))
        
        if index not in [0, 3, 6]: # Movimento para a esquerda
            stateCopy = self.state.copy()
            aux = stateCopy[index-1]
            stateCopy[index-1] = '0'
            stateCopy[index] = aux

            children.append(State(stateCopy, self, 'Move ' + aux + ' para a direita', self.pathLen+1))

        if index not in [6, 7, 8]: # Movimento para baixo
            stateCopy = self.state.copy()
            aux = stateCopy[index+3]
            stateCopy[index+3] = '0'
            stateCopy[index] = aux

            children.append(State(stateCopy, self, 'Move ' + aux + ' para cima', self.pathLen+1))
        
        if index not in [0, 1, 2]: # Movimento para cima
            stateCopy = self.state.copy()
            aux = stateCopy[index-3]
            stateCopy[index-3] = '0'
            stateCopy[index] = aux

            children.append(State(stateCopy, self, 'Move ' + aux + ' para baixo', self.pathLen+1))

        return children
    
    def evaluatePath(self):
        solution = [self]
        while True:
            if solution[-1].parent == None:
                break
            solution.append(solution[-1].parent)
        for state in reversed(solution):
            print(state)
        print('-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('Tamanho do caminho %s' % self.pathLen)
