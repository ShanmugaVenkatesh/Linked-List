# Implementation of Circular Linked List without using tail.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
    
    def display(self):
        temp=self.head
        if temp is None:
            print("Circular Linked list is empty")
        else:
            print(temp.data)
            while temp.next != self.head:
                temp=temp.next
                print(temp.data)

l=CircularLinkedList()

n1=Node(100)
l.head=n1

n2=Node(200)
n1.next=n2

n3=Node(300)
n2.next=n3

n4=Node(400)
n3.next=n4

n4.next=l.head

l.display()