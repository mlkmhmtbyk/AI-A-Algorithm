import math
import random

grid = {0: [1, 5],
        1: [0, 2, 6],
        2: [1, 3, 7],
        3: [2, 4, 8],
        4: [3, 9],
        5: [0, 6, 10],
        6: [5, 1, 7, 11],
        7: [6, 2, 8, 12],
        8: [7, 3, 9, 13],
        9: [8, 4, 14],
        10: [5, 11, 15],
        11: [10, 6, 12, 16],
        12: [11, 7, 13, 17],
        13: [12, 8, 14, 18],
        14: [13, 9, 19],
        15: [10, 16, 20],
        16: [15, 11, 17, 21],
        17: [16, 12, 18, 22],
        18: [17, 13, 19, 23],
        19: [18, 14, 24],
        20: [15, 21],
        21: [20, 16, 22],
        22: [21, 17, 23,],
        23: [22, 18, 24],
        24: [23, 19]
        }

walls = [2,7,12,17]
keepAdding = False
question = input("do you want to add wall into grid? y or n : ")
if(question == 'y'):
        keepAdding = True
while(keepAdding):
    wall = input("plase enter the wall nodes in the grid, enter a number from 0 to 24 : ")
    wall = int(wall)
    walls.append(wall)
    question = input("do you want to add wall into grid? y or n : ")
    if(question == 'n'):
        keepAdding = False

#you can change it to random generation
#initialNode = random.randint(0,24)
#goalNode = random.randint(0,24)
initialNode = 1
goalNode = 18

print("startNode :"),
print(initialNode)
print("goalNode :"),
print(goalNode)

# finds the manhattan distance between input indicies
def Heuristic(source, target):
    x = abs(int(source/5) - int(target/5)) + abs(int(source % 5) - int(target % 5))
    return x

shortestPath = []
visitedList = {}
wallNodes = walls
closedList = walls

infinity = 99999
g = 1
for j in range(25):
    visitedList[j] = infinity
       

def ShortestPath(source, target, grid):
    
    for i in grid[source]:

        f = g + Heuristic(i, target)
        if (i not in closedList):
            visitedList[i] = f

    smallestf = min(visitedList.keys(), key=(lambda k: visitedList[k]))
    
    if ((smallestf != target) and (smallestf != source)):
        if(smallestf not in shortestPath):
            shortestPath.append(smallestf)
        ShortestPath(smallestf, target, grid)
    elif((smallestf != target) and ((smallestf == source) or (smallestf in shortestPath))):
        del visitedList[smallestf]
        closedList.append(smallestf)
        secondSmallestf = min(visitedList.keys(), key=(lambda k: visitedList[k]))
        smallestf = secondSmallestf
        if(smallestf not in shortestPath):
            shortestPath.append(smallestf)
        ShortestPath(smallestf, target, grid)
 
    return shortestPath


path = ShortestPath(initialNode, goalNode, grid)
print("path"), print(path)
print(" ")

startNodeX = int(initialNode % 5)
startNodeY = int(initialNode / 5)

goalNodeX = int(goalNode % 5)
goalNodeY = int(goalNode / 5)


for i in range(5):
    for j in range(5):
        if(i == startNodeY and j == startNodeX):
            print("    S    ", end = '')
        elif(i == goalNodeY and j == goalNodeX):
            print("    G    ", end = '')  
        elif((i * 5)+j in path):
            print("    +    ", end = '')
        elif((i * 5)+j in walls):
            print("    #    ", end = '')
        else:
            print("    *    ", end = '')
    print("")
    print("")
    print("")
    print("")