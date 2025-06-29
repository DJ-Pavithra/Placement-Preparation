# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

def merge(head1,head2):
    dummy=Node(0)
    current=dummy
    while head1 and head2:
        if head1.data<head2.data:
            current.next=head1
            head1=head1.next
        else:
            current.next=head2
            head2=head2.next
        current=current.next
    if head1:
        current.next=head1
    elif head2:
        current.next=head2
    return dummy.next
        
list1=Node(1)
list1.next=Node(2)
list1.next.next=Node(4)

list2=Node(1)
list2.next=Node(3)
list2.next.next=Node(4)

list3=merge(list1,list2)

while(list3):
    print(list3.data,end="->")
    list3=list3.next
print("None")

