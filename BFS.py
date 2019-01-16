graph = {'Ninad': set(['Shrikar', 'Dinesh']),
         'Shrikar': set(['Ninad', 'Advait', 'Anuj']),
         'Dinesh': set(['Ninad', 'Rohan']),
         'Advait': set(['Shrikar']),
         'Anuj': set(['Shrikar', 'Rohan']),
         'Rohan': set(['Dinesh', 'Anuj'])}

def path(graph, st, goal):
    q = [(st, [st])]
    while q:
        (vertex, path) = q.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                q.append((next, path + [next]))

print(list(path(graph, 'Ninad', 'Rohan')))

def shortestpath(graph, st, goal):

        return next(path(graph, st, goal))
