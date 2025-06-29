# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def middle(head):
    count=0
    dummy=head
    while(dummy):
        count +=1
        dummy=dummy.next
    mid=(count+1)//2
    print(mid)
    dummy =head
    for i in range(mid):
        dummy=dummy.next
        
    return dummy
            
        
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)

list1=middle(head)
while(list1):
    print(list1.data,end="->")
    list1=list1.next
print("None")