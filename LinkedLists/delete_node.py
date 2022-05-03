
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



    def delete_node(self,node):
        #Store head node
        current = self.head
        # If the node , we want to delete is the head of link list
        if current is not None:
                if current.value == node:
                    self.head = current.next
                    current = None
                    return
                while (current):
                    if current.value == node:
                        break
                    prev = current
                    current = current.next
        else:
            return
        prev.next = current.next
        current = None

    


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
    llist.delete_node(10)
    print ("\nLinked List after Deletion of 10:")
    llist.print_list()