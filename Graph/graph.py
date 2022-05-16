from collections import deque
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}


#Depth traversal iterative O(n) complexity both for time and space
def depth_first_print(graph,start):
    stack=[start]
    while stack:
        current=stack[-1]
        print(current,end=" ")
        stack.pop()
        for neighbour in graph[current]:
            stack.append(neighbour)

#depth_first_print(graph, "a")

#Recursive depth traversal O(n) complexity
def depth_first_print_rec(graph,current):
    print(current)
    for neighbour in graph[current]:
        depth_first_print_rec(graph,neighbour)


#Iterative Breath First Traversal, complexity 0(n)
def breath_first_print(graph,start):

    queue=deque([start])
    while queue:
        current=queue.popleft()
        print(current,end=" ")
        for neighbour in graph[current]:
            queue.append(neighbour)
#breath_first_print(graph,"a")

# Iterative solution for has_path in graph using breath traversal
def has_path(graph, src, dst):
  stack= [src]
  while stack:
    current = stack[-1]
    stack.pop()
    if current == dst:
      return True
    for neighbour in graph[current]:
      stack.append(neighbour)
    
  return False


# itarative solution for has path in graph using depth traversal
def has_path(graph, src, dst):
  queue=deque([src])
  while queue:
    current= queue.popleft()
    if current==dst:
      return True
    for neighbour in graph[current]:
      queue.append(neighbour)
  return False


#recursive solution for has path using depth travesal logic
def has_path(graph,src,dst):
  if src==dst : return True
  for neighbour in graph[src]:
    if has_path(graph,neighbour,dst) == True:
      return True
  return False

#------------------------------------find undirected_path-----------------------------#
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]
def undirected_path(edges, node_A, node_B):
  #first convert the data, we have into dictionary
  graph = build_graph(edges)
  return has_path(graph,node_A,node_B,set())
  
  
  
def has_path(graph,src,dst,visited):
  if src==dst:
    return True
  
  if src in visited:
    return False
  
  visited.add(src)
  
  for neighbour in graph[src]:
    if has_path(graph,neighbour,dst,visited)==True:
      return True
  return False
    
# Function to remodel the input from list of tuples into adjecent list or dictionary
def build_graph(edges):
    graph={} # empty dict
    for edge in edges:
        #tuple unpacking
        a,b = edge
        #check if we already got the in the dict
        if a not in graph:
          graph[a]=[]
        if b not in graph:
          graph[b]=[]
        #the graph is undirected, so we need to take that into consideration  
        graph[a].append(b)
        graph[b].append(a)
    
    return graph
#undirected_path(edges,'j','m')


# Finding how much connected components there are in a graph
def connected_components_count(graph):
    visited = set()
    count = 0
  
    for node in graph:
        if explore(graph, node, visited) == True:
            count += 1
      
    return count

#Here we define the traverse function, when it is returns false , it means we have finished the elements

def explore(graph, current, visited):
  if current in visited:
    return False
  
  visited.add(current)
  
  for neighbor in graph[current]:
    explore(graph, neighbor, visited)
  
  return True

# Find the largest sized pool in the graph

def largest_component(graph):
    visited=set()
    largest=0
    for node in graph:
        size=explore_size(graph,node,visited)
        if size >largest:
            largest=size
    return largest
  
def explore_size(graph,current,visited):
    if  current in visited:
      return 0
    
    visited.add(current)
    
    size=1
    
    for neighbor in graph[current]:
      size+= explore_size(graph,neighbor,visited)
    
    return size


#Shortest Path function. We use breath first traverse and in the queue we use tuple, to store the number of edges

def shortest_path(edges, node_A, node_B):
  visited=set([node_A])
  graph = build_graph(edges)
  
  #Chosing to use the breath first traversal:
  queue= deque([(node_A,0)])
 
  while queue:
    node, distance=queue.popleft()
    
    if node ==node_B:
      return distance 

    
    
    for neighbor in graph[node]:
      if neighbor not in visited:
        #We store the node in visited to escape the infine loop
        visited.add(neighbor)
        queue.append((neighbor,distance+1))
      
  return -1
  

#--------------------------------------Find island in the grid--------------------------------------#

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]


def island_count(grid):
    visited=set()
    count=0
    #nested loops fo the traversal
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid,r,c,visited)== True:
                count+=1
    return count
    
    
def explore(grid,r , c,visited):
  #defining the boundaries
  row_inbounds = 0<=r<len(grid)
  col_inbounds = 0<=c<len(grid[0])
  #base casses
  if not row_inbounds or not col_inbounds:
    return False
  
  if grid[r][c]=='W':
    return False
  
  pos=(r,c)
  if pos in visited:
    return False
  
  visited.add(pos)
  #Now we check our neighbors
  explore(grid,r-1,c,visited)
  explore(grid,r+1,c,visited)
  explore(grid,r,c-1,visited)
  explore(grid,r,c+1,visited)
  return True


#--------------------------Find smallest island in the grid-----------------------------------#
def minimum_island(grid):
    visited=set()
    min_island=float("inf")
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size=explore_grid(grid,r ,c,visited)
            if 0<size<min_island:
                min_island=size
    return min_island
      
      
  
  
  
  
def explore_grid(grid,r ,c, visited):
  row_inbounds= 0<=r<len(grid)
  col_inbounds=0<=c<len(grid[0])
  
  if not row_inbounds or not col_inbounds:
    return 0
  
  if grid[r][c]=='W':
    return 0
  pos=(r,c)
  if pos in visited:
    return 0
  
  visited.add(pos)
  size=1
  size += explore_grid(grid,r-1,c ,visited)
  size += explore_grid(grid,r+1,c ,visited)
  size += explore_grid(grid,r,c-1 ,visited)
  size += explore_grid(grid,r,c+1 ,visited)
    
  return size