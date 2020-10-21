# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Stack import Stack

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'C'],
    'C': ['E'],
    'D': ['F'],
    'E': ['D', 'F'],
    'F': []
}

weights = {
    'A': {'A': 0, 'B': 2, 'C': 4},
    'B': {'D': 4, 'C': 1, 'E': 2},
    'C': {'E': 3},
    'D': {'F': 2},
    'E': {'F': 2},
    'F': {}
}
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V', 'W', 'X', 'W', 'Z']


# The iterative dfs using a stack :
def iterative_dfs(graph, node):
    print("Starting Iterative DFS traversal")
    stk = Stack()
    # a little bit practice of dictionary comperhension
    visited = {elem: False for elem in graph}
    for nd in graph:
        if not visited[nd]:
            visited[nd] = True
            stk.push(nd)
            helper(graph, node, visited, stk)

## that envelope function helps us to get to every node even if the graph is a forest
def helper(graph, node, visited, stk):
    while not stk.isEmpty():
        curr = stk.Top()
        stk.pop()
        print("Node", curr)

        for children in graph[curr]:
            if not visited[children]:
                visited[children] = True
                stk.push(children)


# the recursive dfs :
def recursive_dfs(graph, source):
    print("Starting recursive DFS traversal")
    visited = {elem: False for elem in graph}
    recursive_helper(graph, source, visited)
    for node in graph:
        if not visited[node]:
            recursive_helper(graph, node, visited)


def recursive_helper(graph, node, visited):
    if not visited[node]:
        print("Node", node)
        visited[node] = True

    for nd in graph[node]:
        recursive_helper(graph, nd, visited)


if __name__ == "__main__":
    print("The Iterative stack Based DFS")
    iterative_dfs(graph, 'A')
    print('The Recursive DFS')
    recursive_dfs(graph, 'A')
