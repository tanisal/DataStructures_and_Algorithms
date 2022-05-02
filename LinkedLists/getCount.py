
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(5)
b = Node(1)
c = Node(30)
d = Node(15)
e = Node(18)
f = Node(20)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


#Length of linked list
def get_count(head):
    count=0
    current=head
    while (current):
        count+=1
        current=current.next
    return count


