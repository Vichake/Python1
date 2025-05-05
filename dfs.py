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


visited = []

def dfs(graph,visited,node):
    if node not in visited:
        print(node," ")
        visited.append(node)

        for side in graph[node]:
            dfs(graph,visited,side)

print(dfs(graph,visited,'A'))