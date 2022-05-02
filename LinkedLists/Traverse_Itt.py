from multiprocessing.sharedctypes import Value


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

def traverse_itt(head):
    current = head
    while (current):
        print(current.value)
        current = current.next

    