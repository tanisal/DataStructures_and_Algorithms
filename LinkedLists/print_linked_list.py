
#------------------------Insertion Methods Linked Lists--------------------------#

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

#Code execution
if __name__ == '__main__':

    #Starts with empty linked list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(5)
    third = Node(16)

    llist.head.next = second
    second.next = third
    
    llist.printList()



    #    


