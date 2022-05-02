
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



# def find_min_max(head):
#     current = head
#     min=0
#     for i in range(lenght_llist(head)-1):
#         next = current.next
#         if current.value > next.value:
#             min = next.value
#             max=current.value
        
#         current = current.next
    
#     return f'min e {min},max e {max}'


# find_min_max(a)
#print(current.value)
# def sort_list(head):
#     head = head
#     while head != None :
#         next = head.next

#         if next.value < head.value:
#             head = next
#             head.next = head
#             print(head.value)
#         else:
#             head=head.next
#     print(head.value)
        
        
        
    
#sort_list(a)

