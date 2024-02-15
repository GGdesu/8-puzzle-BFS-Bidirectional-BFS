import tkinter as tk
from Node import Node
from UninformedSearch import UninformedSearch
import time
from puzzleGui import PuzzleGUI

p1 = [1,2,4,3,0,5,7,6,8]
p2 = [1,2,0,3,4,5,6,7,8]
#print(puzzle)
p3 = [1,2,0,4,3,5,7,6,8]

p4 = [0,4,6,7,3,8,2,1,5]

goalState = [0,1,2,3,4,5,6,7,8]

tempo_inicial = time.time()
StartNode = Node(p=p2)
goalNode = Node(p=goalState)
search = UninformedSearch()

#solution = search.BreadthFirstSearch(initNode)

path = search.bidirectionalBFS(StartNode, goalNode)
tempo_final = time.time()

#inicialização da janela
root = tk.Tk()
root.title("8-Puzzle GUI")

puzzle_states = list()

#pegar apenas os puzzles dos nós
for i in path:
    puzzle_states.append(i.puzzle)

puzzle_gui = PuzzleGUI(root, puzzle_states)

root.mainloop()
#-------------------------------------------

if path:
    print("Caminho da solução:")
    #print(path)
    for i in path:
        i.printPuzzle()
else:
    print("Não foi encontrada uma solução.")

# if( len(solution) > 0):
#     for i in solution:
#         i.printPuzzle()
# else:
#     print("Solução não encontrada")

print("tempo gasto: " + str(tempo_final - tempo_inicial))

