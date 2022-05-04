class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
#Linkilst class, which will contain Node objects
class LinkList():
    def __init__(self):
        self.head = None
    
    def print_list(self):
        current = self.head
        while (current):
            print(current.value)
            current = current.next
        


    def reverse_list(self):
        current = self.head
        prev=None
        while current:
            next = current.next
            current.next=prev
            prev=current
            current=next
        self.head = prev


    #Rerevse via recursion
    def reverse_rec(self):
        def reverse_rec(current, previous=None):
            if current is None: return previous
            next = current.next
            current.next=previous
            return reverse_rec(next,current)
        self.head = reverse_rec(self.head,previous=None)


if __name__ == '__main__':

    llist = LinkList()
    llist.head = Node(1)
    b =  Node(5)
    c = Node(7)
    d = Node(9)
    e = Node(10)

    llist.head.next = b
    b.next = c
    c.next = d
    d.next = e

print('Given list is :')
llist.print_list()
llist.reverse_rec()
print('The reverse one is:')
llist.print_list()