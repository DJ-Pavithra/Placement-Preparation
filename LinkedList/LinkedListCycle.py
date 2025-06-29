# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def hasCycle(head):
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            return True
    head=head.next
    return False
        
head = Node(3)
second = Node(2)
third = Node(0)
fourth = Node(-4)

head.next=second
second.next=third
third.next=fourth
fourth.next=second

res=hasCycle(head)
if(res):
    print("Has cycle")
else:
    print("No cylce")



