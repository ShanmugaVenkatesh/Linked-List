class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        if temp is None:
            print("Double Linkedlist is Empty")
        else:
            while temp:
                print(temp.data)
                temp=temp.next

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

l=DoubleLinkedList()

n1=Node(10) # Previous of n1 --> will be none

l.head=n1   # Making the head to point towards node n1

n2=Node(20) # Creating a node(n2) with data-20, next and prev will be none
n2.prev=n1  # Assigning prev of n2 = n1 
n1.next=n2  # Assigning next of n1 = n2

n3=Node(30)
n3.prev=n2
n2.next=n3

n4=Node(40)
n4.prev=n3
n3.next=n4

# Displaying Double Linked List
l.display()