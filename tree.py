from sys import stdin
from heapq import heappush, heappop

def create_graph(n, m, lines):

    # Create an adjacent empty graph
    graph = [ [] for _ in range(n) ]

    # For each m lines assign the conection nodes into the graph
    for _ in range(m):

        nodes = list(map(int, lines.pop().strip().split()))
        graph[nodes[0]] = nodes[1:]

    return graph

def dfs(l, graph):

    # Create the empty depth and parent lists
    depth = [ 0 for _ in range(len(graph)) ]
    parent = [ i for i in range(len(graph)) ]

    # While exists elements into the stack
    while (len(l)):

        # Get element
        u = l.pop()

        # For each child from u
        for v in graph[u]:
            # Is the node in depther position?
            if (depth[v] < depth[u] + 1):
                # Assign u as parent of v and update the v depth
                parent[v] = u
                depth[v] = depth[u] + 1

            l.append(v)

    return depth, parent

def solve(graph, k): 
    
    # Define the default answer
    ans = 0

    # Create the colors array and the initial color
    colors, color = [ None for _ in range(len(graph)) ], 1

    # Obtain the depth and parents of each node
    depth, parent = dfs([0], graph)

    # Create the queue
    queue = []

    # Get all nodes with depth greater than or equal to k and sort them
    for i in range(len(graph)):
        if (depth[i] >= k): heappush(queue, (depth[i]*-1, i))

    # While there are element into the queue
    while (len(queue)):

        # Obtain the node with greater depth
        _, u = heappop(queue)

        # Check if u is not colored
        if (colors[u] == None):

            # Coloring the node
            colors[u] = color

            # Define the v node and the iterator
            v, i = parent[u], 0

            # As long as there are nodes to be colored
            while i < k and (colors[v] == None):
                colors[v] = color
                v = parent[v]
                i += 1
            
            # Create a new color
            color += 1

            # If already colored all nodes into the trunk, increase the answer
            if i == k: ans += 1

    return ans

def main():

    # Get all lines in the input and reverse the obtained list
    lines = stdin.readlines()
    lines.reverse()

    while (len(lines)):

        # Get the N, M, k values by case
        N, M, k = map(int, lines.pop().strip().split())

        # Create the graph by case
        graph = create_graph(N, M, lines)

        # Print answer
        print(solve(graph, k))

main()