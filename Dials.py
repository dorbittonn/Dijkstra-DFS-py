# Here we will implement Dial's algorithm ,
# this algorithm is optimized version of Dijkstra's algorithm to solve single source shortest path problem.
# this version improve dijkstra's standard preformance from ElogV to E+wV when w is the value of max weight.
# of course this algorithm does better only if the weights are relatively small.
# Programmer : Dor Bitton



def Dials_algo(src, weights):
    INF = float('inf')

    # find the maximum value in order to create the buckets
    maxval = 0
    V = len(weights)
    for w in weights:
        for v in weights[w]:
            maxval = max(weights[w][v], maxval)

    # initialize Buckets as every bucket is a list of nodes, and initializing the returned dictionary 'dist' with the
    # shortest path from source to each node of the graph
    Buckets = [list() for x in range(0, maxval * V + 1)]
    nodes = [x for x in weights]
    dist = {src: 0}
    dist.update({x: INF for x in nodes if x != src})

    
    # we generate wV buckets, the k'th bucket contains all temporarily labels nodes with distance equal to k.
    # The Bucket[wV] is the Infinity Bucket , where all the nodes starts from except the source.
    wV = maxval * V
    Buckets[0].append(src)
    for node in nodes[1:]:
        Buckets[wV].append(node)

    while 1:
        # Scan the buckets until you find a non empty one
        i = 0
        for j in range(0, len(Buckets)):
            if not Buckets[i]:
                i = j

        # Stop term
        if i == wV:
            break

        u = Buckets[i][0]
        # check if every edge from u vertex can improve the current distance, if it is so insert v to its new bucket
        # and take it from infinity Bucket
        for v in weights[u]:
            # calc new distance
            dv = dist[u] + weights[u][v]

            # is it improve the current result?
            if dv < dist[v]:
                if dist[v] == INF:
                    Buckets[wV].remove(v)
                else:
                    Buckets[dist[v]].remove(v)

                dist[v] = dv
                Buckets[dv].append(v)
        Buckets[dist[u]].remove(u)
        print(Buckets)
    return dist


if __name__ == "__main__":

    # Setting the data according to the desired weights
    weights = {
        'A': {'A': 0, 'B': 2, 'C': 4},
        'B': {'D': 4, 'C': 1, 'E': 2},
        'C': {'E': 3},
        'D': {'F': 2},
        'E': {'F': 2},
        'F': {}
    }
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E', 'F'],
        'C': ['E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }

    print(Dials_algo('A', weights))
