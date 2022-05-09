from collections import deque

#Create a Node class, which we will use for our binery tree
class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
a = Node(5)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)
g= Node(19)
j= Node(35)
h=Node(20)

a.left= b
a.right = c
b.left = d
b.right = e
#e.left =j
e.right=h 
f.left=g
c.left = f
c.right=j




# Iterative Solution
def depthFirstValues(root):
    if root is None:
        return []
    values=[]
    stack=[root]
    while stack:
        current = stack.pop()
        values.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return values

#depthFirstValues(a)


#Recursive Solution
def depthFirstValues_Rec(root):
    if root is None: return []
    left_values = depthFirstValues_Rec(root.left)
    right_values = depthFirstValues_Rec(root.right)
    return [root.val,*left_values,*right_values]

#Iteration Solution with O(n) complexity using deque as inserting the fornt of the queue
def breathFirstValues(root):
    queue = deque([root])
    values=[]
    while queue:
        current = queue.pop()
        values.append(current.val)
        if current.left:
            queue.appendleft(current.left)
        if current.right:
            queue.appendleft(current.right)
    return values

#breathFirstValues(a)




#Iterative sum of the tree
def sumTree(root):
    if root is None:
        return 0
    sum=0
    stack=deque([root])
    while stack:
        current = stack.pop()
        sum+=current.val
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return sum

#Recursive Sum of tree
def sumTree_rec(root):
    if root is None: return 0
    return root.val + sumTree_rec(root.left) + sumTree_rec(root.right)
#sumTree(a)


# Iterative if tree includes a target
def tree_inludes(root,target):
    if root is None: return False
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.val == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False

# Recursive Solution tree includes  s target
def  tree_includes_rec(root,target):
    if root is None: return False
    if root.val == target: return True
    return tree_includes_rec(root.left,target) or tree_includes_rec(root.right,target)


# Iterative solution for mininum value of a tree with a given root
def tree_min_value(root):
    min_value = float('inf')
    queue = deque([root])
    while queue:
        current=queue.popleft()
        if min_value > current.val:
            min_value=current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return min_value



# Recursive solution
def tree_min_value_rec(root):
    if root is None: return float('inf')
    return min(root.val,tree_min_value_rec(root.left),tree_min_value_rec(root.right)) 

   

# Recursive maxSum solution
def maxSum_rec(root):
    """ return the maximum sum of any root to leaf path """
    if root is None: return float("-inf")
    if root.left is None and root.right is None: return root.val
    return max(root.val + maxSum_rec(root.left),root.val + maxSum_rec(root.right))

#Print all path to the leafs, when having the root of a tree
def all_paths(root,paths):
    if root is None: 
        return False
    paths.append(root.val)
    
    if all_paths(root.left,paths) and all_paths(root.right,paths):
        return True
    paths.pop()
    return True

def print_all_paths(root):
    paths=[]
    if all_paths(root,paths):
        for i in range(len(paths)-1):
            print(paths[i] , end="->")
        print(paths[len(paths)-1])
    else:
        print('No paths')
#print_all_paths(a)





#Find a path from root to a given target recursively
def tree_path(root,arr,target):

    if root is None:
        return False

    arr.append(root.val)

    if root.val  == target:
        return True

    if tree_path(root.left,arr,target) or tree_path(root.right,arr,target):
        return True
    arr.pop(-1)
    return False

def print_tree_path(root,target):
    arr=[]
    if tree_path(root,arr,target):
        for i in range(len(arr)-1):
            print(arr[i] ,end = "->")
        print(arr[len(arr)-1])
    else:
        print("there is no Path")

# Height of a tree, or  maxdepth recursively
def height_tree_rec(root):
    if root is None: return -1
    return 1 + max(height_tree_rec(root.left),height_tree_rec(root.right))

# Number of nodes in binary tree
def number_nodes(root):
    if root is None: return 0
    return 1+number_nodes(root.left)+number_nodes(root.right)
#number_nodes(a) 

#Number of leaf nodes in binary tree
def number_leaf_nodes(root):
    if root is None: return 0
    if root.left is None and root.right is None: return 1
    return number_leaf_nodes(root.left) + number_leaf_nodes(root.right)
#number_leaf_nodes(a)

#Print elements at a given level . Bad complexity O(n2)
def print_given_level_rec(root,level):
    if root is None: return
    if level ==1: 
        print(root.val, end=" ")
        return
    print_given_level_rec(root.left, level-1)
    print_given_level_rec(root.right,level-1)

#print_elements_at_level(a,1)

#Print all the elements at a given level of the tree, iterative
def print_all_elements(root):
    if root is None:
        return
    queue=deque([root])
    while queue:
        print(queue[0].val,end=" ")
        current= queue.popleft()
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
#print_all_elements(a)

#Print all the elements in the tree but by level order: complexty O(n)
def print_all_level_order(root):
    if root is None: return
    queue= deque([root])
    while queue:
        count=len(queue)
        while count:
            current= queue.popleft()
            print(current.val,end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            count-=1
        print(" ")

#print_all_level_order(a)

#Printing the nodes at agiven level, solution is iterative . complexity O(n)
def print_elements_at_given_level(root,klevel):
    if root is None: return
    queue = deque([root,None]) #We add the second None, to keep track when to add to the level
    level=1
    while queue:
        current= queue.popleft()
        if level == klevel and current:
            print(current.val, end=" ")
        if current== None:
            if queue:
                queue.append(None)
            level+=1
            if level>klevel:
                break
        else:
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    print(" ")

#print_elements_at_given_level(a,5)


# Reverse level order with recursion
def reverse_level_order_rec(root):
    if root is None: return
    height=height_tree_rec(root)

    for i in range(height+1,0,-1):
        print_elements_at_given_level(root,i)

# Reverse level order with iteration
def reverse_level_order(root):
    stack=deque([])
    queue=deque([root])
    while queue:
        current=queue.popleft()
        stack.appendleft(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return stack

#Print the left side of the binary tree
def left_side(root):
    queue=deque([root])
    while len(queue): 
        n= len(queue) # Number of nodes at current level
        for i in range(1,n+1): #Traversing through the node line
            current = queue.popleft()
            if i==1:
                print(current.val, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


# Average Sum bu level order, traverse method with 2 Queues
def average_sum_level_order(root):
    if root is None: return
    queue1=deque([root])
    queue2=deque([])
    while queue1 or queue2:
        sum_q1=0
        count=0
        while queue1:
            current=queue1.popleft()
            sum_q1 += current.val
            count+=1
            if current.left:
                queue2.append(current.left)
            if current.right:
                queue2.append(current.right)
        print(sum_q1/count)
        sum_q1=0

        sum_q2=0
        count=0
        while queue2:
            current=queue2.popleft()
            sum_q2 += current.val
            count+=1
            if current.left:
                queue1.append(current.left)
            if current.right:
                queue1.append(current.right)
        print(sum_q2/count)
        sum_q2= 0
    
#average_sum_level_order(a)  

# Mirror a binary tree
def mirror_tree(root):
    if root is None: return
    left =root.left
    root.left=root.right
    root.right=left

    mirror_tree(root.left)
    mirror_tree(root.right)

#mirror_tree(a)
#print_all_elements(a)  

# height of a tree itaratively
def height_itt(root):
    if root is None: return 0
    queue=deque([root])
    height=0
    while queue:
        num_nodes=len(queue)
        height+=1
        while num_nodes:
            current=queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            num_nodes-=1
    print(height)
height_itt(a)