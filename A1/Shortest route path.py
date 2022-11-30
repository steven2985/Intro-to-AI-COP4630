"""This program helps to find the shortest route between different cities to Bucharest
with the help of three different algorithms BFS, DFS, and A*"""

graph = {
   'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Bucharest': ['Urziceni', 'Giurgiu', 'Pitesti', 'Fagaras'],
    'Craiova': ['Dobreta', 'Pitesti', 'Rimnicu Vilcea'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Eforie': ['Hirsova'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Giurgiu': ['Bucharest'],
    'Hirsova': ['Eforie', 'Urziceni'],
    'Iasi': ['Neamt', 'Vaslui'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Neamt': ['Iasi'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Pitesti': ['Rimnicu Vilcea', 'Bucharest', 'Craiova'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Sibiu': ['Rimnicu Vilcea', 'Fagaras', 'Arad', 'Oradea'],
    'Timisoara': ['Lugoj', 'Arad'],
    'Urziceni': ['Bucharest', 'Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Zerind': ['Oradea', 'Arad'],
}
heuristic = {
    'Arad':366,
    'Bucharest':0,
    'Craiova':160,
    'Dobreta':242,
    'Eforie':161,
    'Fagaras':178,
    'Giurgiu':77,
    'Hirsova':151,
    'Iasi':226,
    'Lugoj':244,
    'Mehadia':241,
    'Neamt':234,
    'Oradea':380,
    'Pitesti':98,
    'Rimnicu Vilcea':193,
    'Sibiu':253,
    'Timisoara':329,
    'Urziceni':80,
    'Vaslui':199,
    'Zerind':374
    }

visitedB = [] # List to keep track of visited nodes.
visitedD = set() # Set to keep track of visited nodes.
visitedA = set()
queue = []     #Initialize a queue
stack = []
def calculateCost():
    print("")
def BFS (visited, graph, node):
     visited.append(node[0])
     queue.append(node)
     while queue:
         s = queue.pop(0) 
         print (s, "\n") 
         if s == 'Bucharest':
             break
         for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
 

def DFS(visited, graph, node):
    stack.append(node)
    while stack:
        current = stack.pop(0)
        if current not in visited:
            print (current)
            visited.add(current)
            if current == 'Bucharest':
               break
            else:
                for neighbour in graph[current]:
                    current = neighbour
                    stack.append(neighbour)
    
def A (node):
    stack.append(node)
    came_from: dict[node, float] = {}
    came_from[start] = None
    costSoFar: dict(node, float) = {}
    costSoFar[node] = 0
    newCost = 0
    while stack:
        current = stack.pop(0)
        if current not in visitedA:
            print(current)
            visitedA.add(current)
            if current == 'Bucharest':
                break
            else:
                for neighbour in graph[current]:
                    newCost = costSoFar[current] + heuristic[current]
                    if next not in costSoFar or newCost < costSoFar[next]:
                        costSoFar[next] = newCost
                        priority = newCost + heuristic[current]
                        print(priority)
                        came_from[next] = current
                        newCost += costSoFar[current]
                    


while appOption != "q":
    if appOption == "m":
        print("This app will help you to find the shortest route to Bucharest using three different algorithms BFS, DFS, and A*.")
        print("Have a good trip and enjoy this app. Do not forget to give it a 5 start review on the Play Store.")
        start = input("Enter the city you are departing from: ")
        alg = input("Which algorithm would you like to use bfs, dfs, or a: ")
        if(alg == "bfs"):
            BFS(visitedB, graph, start)
        elif(alg == "dfs"):
            DFS(visitedD, graph, start)
        elif(alg == "a"):
            A(start)
        elif(alg == "q"):
            print("Thank you for using the mapping feature.")
        else:
            alg = input("Invalid input.")
    elif appOption == "t":
        TicTacToe()
    else:
        print("Invalid input")
    appOption = input("Which app would you like to use Map (m) or Tic Tac Toe (t) or q to quit: ")
        