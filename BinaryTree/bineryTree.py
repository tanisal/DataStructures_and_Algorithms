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
e = Node(-2)
f = Node(1)


a.left= b
a.right = c
b.left = d
b.right = e
c.left = f

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
sumTree(a)
