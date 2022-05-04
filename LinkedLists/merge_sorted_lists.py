class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
# The dame as Linkilst class, chich will contain Node objects
class LinkList():
    def __init__(self):
        self.head = None
    
    def print_list(self):
        current = self.head
        while (current):
            print(current.value)
            current = current.next
    


def merge_list(head1,head2):
    #pointer to the first list
    current1 = head1
    #pointer to the head of the second list
    current2 = head2
    #Creating a dummy Node
    dummy_node = Node(0)
    tail = dummy_node
    
    while (True):
        #Checking for the edge cases
        if not current2: 
            tail.next = current1 
            break

        if not current1:
            tail.next = current2
            break
        
        if current1.value < current2.value:
            tail.next=current1
            current1=current1.next
        else:
            tail.next= current2
            current2=current2.next
        tail= tail.next

    return dummy_node.next

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

    
    
    llist2 = LinkList()
    llist2.head = Node(3)
    r = Node(4)
    s = Node(6)
    t = Node(8)
    
    llist2.head.next=r
    r.next = s
    s.next = t

    print ("Created Linked List: ")
    llist.head = merge_list(llist.head,llist2.head)
    llist.print_list()
   