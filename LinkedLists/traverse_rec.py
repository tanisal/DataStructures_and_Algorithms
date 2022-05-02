
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.next = b
b.next = c
c.next = d
d.next = e


def traverse_rec(head):
    if head == None : return None
    print(head.value)
    return traverse_rec(head.next)
