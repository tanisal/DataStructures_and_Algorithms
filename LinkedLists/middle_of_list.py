# Node Class
class Node():

    #Function to initialise the Node object
    def __init__(self,value):
        self.value = value
        self.next = None

# Linked List Class contains a Node Object
class LinkedList():
    #Function to initialise head
    def __init__(self):
        self.head=None
        
 
    def printList(self):
        current = self.head
        while (current):
            print(current.value)
            current=current.next


    def middle_list(self):
        #Setting slow and fast pointer to the head. The fast pointer is 2 times faster.
        slow_pointer = self.head
        fast_pointer = self.head
        # When the fast pointer is at the end of the list, the slow pointer is at the middle
        while fast_pointer and fast_pointer.next:
            slow_pointer=slow_pointer.next
            fast_pointer=fast_pointer.next.next
        return slow_pointer.value



#Code execution
if __name__ == '__main__':

    #Starts with empty linked list
    

    llist = LinkedList()
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
llist.printList()
print('Middle is:')
llist.middle_list()