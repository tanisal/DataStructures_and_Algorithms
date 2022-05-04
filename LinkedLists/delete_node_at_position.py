#Initialising Node class
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
    
    #Iterative remove node at position
    def delete_node_at_position(self,position):
        
        current = self.head

        if position == 0:
            self.head=current.next
            current=None
        
        count = 0
        prev=None
        while current and position!=count:
            prev=current
            count+=1
            current=current.next
        
        if current is None:
                return
        
        prev.next=current.next
        current= None

# # Recursively delete node at k position

def delete_node_rec(head,k):
    if k ==1 : return head.next
    if k<0 : return head
    if head == None:
            return
    head.next = delete_node_rec(head.next,k-1)
    return head


if __name__ == '__main__':
    llist = LinkList()
    llist.head = Node(7)
    second = Node(19)
    third = Node(10)
    fourth = Node(14)
    fifth = Node(5)

    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    print ("Created Linked List: ")
    llist.print_list()
    llist.delete_node_at_position(0)
    print ("\nLinked List after Deletion of position n:")
    llist.print_list()