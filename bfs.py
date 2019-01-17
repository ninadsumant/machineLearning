'''
         A
       /   \
      C     B
     / \    / \
    D   E   F  G

'''

dict={'A':{'B','C'},
      'B':{'D','E','A'},
      'C':{'F','G','A'},
      'D':{'B'},
      'E':{'B'},
      'F':{'C'},
      'G':{'C'},
      }
print(dict)
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
            print(vertex,next) #Remove ,this line is just for understanding
        print("-") #Remove ,this line is just for understanding
    
s=input("Enter Starting node : ")
e=input("Enter Ending node : ")
lst=list(bfs_paths(dict, s,e))

if(len(lst)>0):
    print(lst[0])
else:
    print("No connection found")
