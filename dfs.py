'''
         A
       /   \
      C     B
     / \    / \
    D   E   F  G

'''
graph2 = {
    'A' : ['B','C'],
    'B' : ['A','D','E'],
    'C' : ['A','F','G'],
    'D' : ['B'],
    'E' : ['B'],
    'F' : ['C'],
    'G' : ['C'],
}
visited = []
def dfs(graph,node):
    global visited  
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n)

dfs(graph2,'A')
print(visited)
