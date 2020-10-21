# This program will get a graph from the user and execute one of 3 algorithms
# desired graph algorithm on it
# This little project's main target is to practise python, and learn how to use new algorithm like Dial's algorithm
# Dial algorithm is optimized Dijkstra version

# Imports
import DFS
import Dials
INF = float('inf')


# The following function receive a father node and assign a child from the user to it
def GetChildren(graph, father):
    print("Enter the Node ", father, "'s children splited by commas, for example: ""B,X,D ")
    children_dict = {}
    print(graph)
    # obtain children dict from user

    children_dict = {x.capitalize() if (x.isalpha() or not x)
                     else print("no children inserted.")
                     for x in input().split(',')}
    # After checking children are valid attach them to graph
    # make sure that there are not self edges
    for child in children_dict:
        if child == "":
            continue
        while child == father:
            child = input("No self edges! Insert a node instead:").capitalize()
        while not in_Graph(graph, child):
            child = input().capitalize()
        # The following statement ensures no null or empty spaces inside the graph
        if child is not None and child != father:
            graph[father][child.capitalize()] = INF

    # Makes every node in the graph unique and avoid having the same node multiple times
    # graph[father] = dict(set(graph[father]))


# The following function recieve a graph and set weights to every edge according to the user's request
def SetWeights(graph, node):
    for neighbour in graph[node]:
        txt = "Please enter the weight from " + node + " to " + neighbour+" "
        graph[node][neighbour] = GetDigitfromUser(txt)


# The following function will ensure that the a certain node indeed exists in the graph
def in_Graph(graph, element):
    for node in graph:
        if node == element:
            return True
    print("There's No node ", element, " in the graph, try another one:")
    return False


# The following function will recieve an integer from the user
def GetDigitfromUser(text):
    digit = input(text)
    while not digit.isdigit():
        digit = input("enter a number! ")

    digit = int(digit)
    return digit


# DFS algo's support different kind of graph representation so I process the weighted graph to a non weighted one
# before sending it
def process_Graph(Graph):
    g = {}
    for i in range(0, len(Graph)):
        lst = [k for k in Graph[ABC[i]]]
        g[ABC[i]] = lst
    return g


##     Main    ###

ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V', 'W', 'X', 'W', 'Z']

print("Welcome to GraphsAreFun!\n"
      "please think of directed graph with integer weights first\n"
      "NOTE : the the graph's nodes is represented by capital letters only")
size = int(GetDigitfromUser("Please Enter your desired Graph size - 2-26 "))

# Initializing an empty graph
Graph = { ABC[i]: {} for i in range(0, size) }

# Attaching children to their parents
for i in range(0, size):
    GetChildren(Graph, ABC[i])
    SetWeights(Graph, ABC[i])

while 1:
    algo = GetDigitfromUser("Choose which of the following graph algorithms you would like to run\n1 - Iterative DFS\n"
                            "2 - Recursive DFS\n"
                            "3 - Dial's Algorithm - (Optimized Dijkstra)\n"
                            "4 - Show graph representation")

    source = input("Choose a source node for the algorithm to start with").capitalize()
    while not in_Graph(Graph, source):
        source = input().capitalize()

    if algo == 1:
        # if one of the DFS options are selected we need to
        # change the format of the graph obtained from key:list to key:dict
        g = process_Graph(Graph)
        DFS.iterative_dfs(g, 'A')
    elif algo == 2:
        g = process_Graph(Graph)
        DFS.recursive_dfs(g, 'A')
    elif algo == 3:
        print("shortest distances from", source, "to all vetices is:\n", Dials.Dials_algo(source, Graph) )
    elif algo == 4:
        print(Graph)
