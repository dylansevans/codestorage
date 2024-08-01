def bfs(graph, root):
  visited_nodes = set()
  visited_nodes.add(root)
  neighbors_queue = [root]

  while neighbors_queue:
    vertex = neighbors_queue.pop(0)

    print(f"{str(vertex)} ", end =" ")

    for neighbour in graph[vertex]:
      if neighbour not in visited_nodes:
          neighbors_queue.append(neighbour)
          visited_nodes.add(neighbour)

def bfs_path(graph, root, target):
    
    path_queue = [[root]]
   
    while path_queue: #ie. len(path_queue) > 1
        #take the first path from the path_queue
        old_path = path_queue.pop(0) 
        #start from the last node in that path
        last_node = old_path[-1] 
        
        #consider each neighbor of the last node in the path being considered
        for neighbour in graph[last_node]:
            #if the neighbor hasn't been considered yet     
            if neighbour not in old_path: 
                #add a new path to the list of paths to consider
                new_path = old_path.copy()
                new_path.append(neighbour)
                path_queue.append(new_path) 

            # first time you find the target gives you "a" shortest path
            if neighbour == target:
                return tuple(new_path)
    
    return tuple() #no path exists
            
if __name__ == "__main__":

    binary_tree_graph ={
       'A':['B'],
       'B':['F','A','D'],
       'C':['D'],
       'D':['B','C','E'],
       'E':['D'],
       'F':['B', 'G'],
       'G':['F','I'],
       'H':['I'],
       'I':['G', 'H']
    }
    print("BFS Traversal: ", end =" ")
    bfs(binary_tree_graph, 'F')
    print()
    print("BFS Path: ",bfs_path(binary_tree_graph, 'F','E' ))
    # print("BFS Path: ",bfs_path(binary_tree_graph, 'A','I' ))
    # print("BFS Path: ",bfs_path(binary_tree_graph, 'H','C' ))

    
    #Dinner Examples
    friends = {
        'Alice':['Bob'],
        'Bob':['Alice', 'Eve'],
        'Eve':['Bob']
    }
    # print("BFS Traversal: ", end =" ")
    # bfs(friends, 'Alice')
    # print()

    friends_disconnected = {
        'Asa':[], 
        'Bear':['Cate'],
        'Cate':['Bear', 'Dave'],
        'Dave':['Cate','Eve'], 
        'Eve':['Dave'], 
        'Finn':['Ginny', 'Haruki', 'Ivan'], 
        'Ginny':['Finn','Haruki'], 
        'Haruki':['Ginny'], 
        'Ivan':['Finn']
    }
    # print("BFS Traversal of Disconnected Graph: ", end =" ")
    # bfs(friends_disconnected, 'Bear')
    # print()
    # print("BFS Traversal of Disconnected Graph:: ", end =" ")
    # bfs(friends_disconnected, 'Finn')
    # print() 
    # print("BFS Path: ", bfs_path(friends_disconnected,'Haruki', 'Ivan'))    