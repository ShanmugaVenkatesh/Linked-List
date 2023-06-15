class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def display(self):
        temp=self.head
        if temp is None:
            print("Circular Linked list is empty")
        else:
            print(temp.data)
            while temp.next != self.head:
                temp=temp.next
                print(temp.data)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

l=CircularLinkedList()

n1=Node(10)

# Initially head and tail points to the same node or first created node(n1) and then
# head --> points always to the first node and 
# tail --> when node is added into the circular linked list, tail points to the newly added node or last node of the circular linked list

# Initially, when CLL contain one node --> both head and tail points to that node.
l.head=n1
l.tail=n1
# Due to one node present in CLL, its address part should contain the 1st node address. Here it contains its own address.
# l.tail.next=l.head

n2=Node(20)
l.tail.next=n2  # tail here points to the n1. So, tail.next--> n2 (next node)
l.tail=n2         # Assigning the tail to the node n2

n3=Node(30)
l.tail.next=n3
l.tail=n3

n4=Node(40)
l.tail.next=n4
l.tail=n4

# Assigning the address part of the last node(n4) as 1st node address
l.tail.next=l.head
l.display()