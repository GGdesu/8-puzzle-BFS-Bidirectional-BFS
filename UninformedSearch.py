
class UninformedSearch:

    def __init__(self):
        pass
        

    def BreadthFirstSearch(self, rootNode):
        pathToSolution = list()
        openList = list()
        closedList = list()

        openList.append(rootNode)
        goalFound = False

        while(len(openList) > 0 and (not goalFound) ):

            currentNode = openList[0]
            closedList.append(currentNode)
            openList.pop(0)

            currentNode.expandNode()

            for i in currentNode.children:
                
                currentChild = i
                if(currentChild.GoalTest()):
                    print("goal found")
                    goalFound = True
                    self.pathTrace(pathToSolution, currentChild)
                    break
                
                if not self.contains(openList, currentChild) and not self.contains(closedList, currentChild):
                    openList.append(currentChild)



        return pathToSolution
    
    def bidirectionalBFS(self, startNode, goalNode):
        
        pathSolution = list()

        startOpenList = list()
        startClosedList = list()
        startOpenList.append(startNode)

        goalOpenList = list()
        goalClosedList = list()
        goalOpenList.append(goalNode)


        while startOpenList and goalOpenList:
            
            startCurrentNode = startOpenList[0]
            startClosedList.append(startCurrentNode)
            startOpenList.pop(0)

            goalCurrentNode = goalOpenList[0]
            goalClosedList.append(goalCurrentNode)
            goalOpenList.pop(0)

            #expandir os nós no sentido start-to-goal
            
            startCurrentNode.expandNode()
            for startChild in startCurrentNode.children:

                if(self.contains(goalClosedList, startChild)):
                    print("objetivo encontrado no sentido start-to-goal ")
                    goalNode = self.getEQNode(goalClosedList,startChild)
                    pathSolution = self.reconstructionBidirectionaPath(startChild, goalNode)
                    return pathSolution
                
                if startChild not in startOpenList and startChild not in startClosedList:
                    startOpenList.append(startChild)

            #expandir os nós no sentido goal-to-start
            goalCurrentNode.expandNode()
            for goalChild in goalCurrentNode.children:

                if(self.contains(startClosedList, goalChild)):
                    print("objetivo encontrado no sentido goal-to-start")
                    startNode = self.getEQNode(startClosedList, goalChild)
                    pathSolution = self.reconstructionBidirectionaPath(startNode, goalChild)
                    return pathSolution
                
                if goalChild not in goalOpenList and goalChild not in goalClosedList:
                    goalOpenList.append(goalChild)
        return None
    
    def contains(self, nodeList, node):
        
        for i in nodeList:
            
            if (i.isSamePuzzle(node.puzzle)):
                return True
                #print(i.puzzle)
                #print(node.puzzle)
                
                #print(contain)
        #print(str(contain) + " contain")

    #def goalTest(self, ):
            
    def reconstructionBidirectionaPath(self, instersecStartNode, intersecGoalNode):
        
        pathStart = list()
        pathGoal = list()

        print("building path...")
        self.pathTrace(pathStart, instersecStartNode)
        pathStart.reverse()

        self.pathTrace(pathGoal, intersecGoalNode)
        pathGoal.pop(0)

        combined_path = pathStart + pathGoal

        return combined_path



    
    def pathTrace(self, path, n):
        #print("tracing path...")
        current = n
        path.append(current)

        while( current.parent != None):
            current = current.parent
            path.append(current)
    
    def getEQNode(self, nodeList, node):
        for i in nodeList:
            if (i.isSamePuzzle(node.puzzle)):
                return i
