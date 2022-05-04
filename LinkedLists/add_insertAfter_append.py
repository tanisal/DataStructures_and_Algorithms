
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

    # Function to print the linked list
    def printList(self):
        current = self.head
        while (current):
            print(current.value)
            current=current.next

    # Function to insert new node at the beginning
    def add_infront(self,new_data):
        #Initialising the new node
        new_node = Node(new_data)
        # Assigning the next node of the new node to be the previuos head
        new_node.next = self.head
        # Assigning the new head to be the new node
        self.head= new_node

    def insert_node_after(self,prev,new_data):
        #Check if the previous node is in the list
        if prev is None:
            print ('Previous node must be in the list')
            return
        # Creating the new node object
        new_node = Node(new_data)
        # Assigning the next of the new node to be the next of previuos node
        new_node.next = prev.next
        # The next of the previuos node becomes the new node
        prev.next=new_node

    def append(self,new_data):
        # Creating the new node object
        new_node = Node(new_data)
        
        #Checking if the the node is None
        if self.head is None:
            #Then set the new node as the next to the old one
            self.head = new_node
            return
        else:
            # otherwise we set the current node
            current=self.head
            #till the current node exists:
            while (current.next):
                # We traverse trough the list
                current = current.next
            # And when we go to the end of it we assign the next node to be the new one
            current.next=new_node

#Code execution
if __name__ == '__main__':

    #Starts with empty linked list
    llist = LinkedList()

    llist.add_infront(6)

    llist.add_infront(12)

    llist.append(27)

    llist.insert_node_after(llist.head.next,54)

    llist.printList()

       


