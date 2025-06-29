# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def reverse(head):
    prev=None
    current=head
    
    while current:
        nextNode = current.next
        # Reverse the link
        current.next= prev
        # Move one step ahed
        prev,current=current,nextNode
    
    head=prev
    return head

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)

reversedList=reverse(head)

while(reversedList):
    print(reversedList.data,end="->")
    reversedList=reversedList.next
print("None")
    