# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
# Input: head = [1,1,2]
# Output: [1,2]

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def remove(head):
    current=head
    while current and current.next:
        if current.data==current.next.data:
            current.next=current.next.next
        else:
            current=current.next
    return head
        
        
head=Node(1)
head.next=Node(1)
head.next.next=Node(2)

list1=remove(head)

while(list1):
    print(list1.data,end="->")
    list1=list1.next
print("None")