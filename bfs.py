graph = {
    'A':['B','C','D'],
    'B':['E','F'],
    'C':['G','H'],
    'D':['I'],
    'E':['J','K'],
    'F':[],
    'G':['L'],
    'H':[],
    'I':['M'],
    'J':[],
    'K':['N'],
    'L':[],
    'M':[],
    'N':[]
}

target = 'G'
visited = []
queue = []
path = {}
def bfs(graph,visited,node,goal):
    visited.append(node)
    queue.append(node)
    path[node] = None
    while queue:
        e = queue.pop(0)
        print(e)
        if e == goal:
            break
        for i in graph[e]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                path[i] = e

print("BFS Traversal: ")
bfs(graph,visited,'A','G')

