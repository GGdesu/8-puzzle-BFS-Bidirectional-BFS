
import copy

class Node:

    #iniciando atributos da classe
    def __init__(self, p):
        
        #lista de filhos desse nó ou proximos caminhos do nó
        self.children = list()

        #pai desse nó, o raiz
        self.parent = None

        #lista comm o quebra cabeça do nó
        self.puzzle = p
        

        #num de colunas
        self.col = 3
        
        #utilizando o setter para modificar o puzzle
        #self.setPuzzle(puzzle)
        
        self.zeroIndex = 0
        #self.printPuzzle()


    #verifico se o quebra cabeça atual é o desejado
    def GoalTest(self):
        isGoal = False
        # Quebra cabeça desejado
        # 0 1 2
        # 3 4 5
        # 6 7 8
        goalPuzzle = [0,1,2,3,4,5,6,7,8]
        temp = copy.deepcopy(self.puzzle)
        #print(temp)
        if (temp == goalPuzzle):
            isGoal = True
        #print(str(isGoal) + "isgoal")
        return isGoal
    
    def expandNode(self):

        #descobrir o indice do valor 0
        for i in range(len(self.puzzle)):
            if(self.puzzle[i] == 0):
                self.zeroIndex = i
        
        self.moveToRight()
        self.moveToLeft()
        self.moveToUp()
        self.moveToDown()

    #movimentaçao dos nós
    def moveToRight(self):

        if(self.zeroIndex % self.col < self.col - 1):
            tempPuzzle = copy.deepcopy(self.puzzle)

            #mudar a posição dos valores no quebra cabeça
            tempValue = tempPuzzle[self.zeroIndex + 1]
            tempPuzzle[self.zeroIndex + 1] = tempPuzzle[self.zeroIndex] 
            tempPuzzle[self.zeroIndex] = tempValue
            
            # self.printPuzzle()
            # print(tempPuzzle)
            # self.isSamePuzzle(self.puzzle)

            #cria um filho e adiciona a lista de filhos do nó atual
            #adiciona o nó atual como pai do nó filho criado agora.
            child = Node(tempPuzzle)
            self.children.append(child)
            child.parent = self


    def moveToLeft(self):

        if(self.zeroIndex % self.col > 0):
            tempPuzzle = copy.deepcopy(self.puzzle)
            #print(tempPuzzle)

            tempValue = tempPuzzle[self.zeroIndex - 1]
            tempPuzzle[self.zeroIndex - 1] = tempPuzzle[self.zeroIndex]
            tempPuzzle[self.zeroIndex] = tempValue
            #print(tempPuzzle)

            child = Node(tempPuzzle)
            self.children.append(child)
            child.parent = self

    def moveToUp(self):

        if(self.zeroIndex - self.col >= 0):
            tempPuzzle = copy.deepcopy(self.puzzle)
            

            tempValue = tempPuzzle[self.zeroIndex - 3]
            tempPuzzle[self.zeroIndex - 3] = tempPuzzle[self.zeroIndex]
            tempPuzzle[self.zeroIndex] = tempValue
            

            child = Node(tempPuzzle)
            child.parent = self
            self.children.append(child)
            

    def moveToDown(self):

        if(self.zeroIndex + self.col < len(self.puzzle)):
            tempPuzzle = copy.deepcopy(self.puzzle)
            #self.printPuzzle()
            #print(tempPuzzle)

            tempValue = tempPuzzle[self.zeroIndex + 3]
            tempPuzzle[self.zeroIndex + 3] = tempPuzzle[self.zeroIndex]
            tempPuzzle[self.zeroIndex] = tempValue
            #print(tempPuzzle)

            child = Node(tempPuzzle)
            self.children.append(child)
            child.parent = self
            

    def printPuzzle(self):
        
        print()
        index = 0

        for i in range(self.col):
            for j in range(self.col):
                print( str(self.puzzle[index]), end=' ')
                index += 1
            print()

    def isSamePuzzle(self, p2):
        
        if(self.puzzle == p2):
            return True
        
        #print(samePuzzle)

        


    
    
    #setter
    def setPuzzle(self, p):
        self.puzzle = copy.deepcopy(p)
        
    # def reconstructBidirectionalPath(self, startNode, goalNode, intersectionNode):
    #     pathFromStart = self.pathTrace([], intersectionNode, startNode)
    #     pathFromGoal = self.pathTrace([], intersectionNode, goalNode)
    #     pathFromGoal = pathFromGoal[:-1]
    #     fullPath = pathFromStart + pathFromGoal[::-1]
    #     return fullPath

    # def pathTrace(self, path, startNode, endNode):
    #     current = startNode
    #     path.append(current)
    #     while current.parent and current != endNode:
    #         current = current.parent
    #         path.append(current)
    #     return path[::-1]
    
   
