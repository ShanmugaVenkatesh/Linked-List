class SingleLinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        if temp is None:
            print("Linked list is empty")
        else:
            while temp:
                print(temp.data)
                temp=temp.next

    # Deletion at begining
    def DeletionAtBegining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    # Deletion at End
    def DeletionAtEnd(self):
        temp=self.head.next     # Creating a variable (temp) and storing the address of the next address of the head
        prev=self.head          # Creating a variable (prev) and storing the address of the head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None 

    # Deletion at specific position
    def DeletionAtPosition(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

l=SingleLinkedList()

n1=Node(10)
l.head=n1

n2=Node(20)
n1.next=n2

n3=Node(40)
n2.next=n3

n4=Node(22)
n3.next=n4

n5=Node(4)
n4.next=n5

# Deletion At the Begining
l.DeletionAtBegining()

# Deletion At End
l.DeletionAtEnd()

# Deletion At Specific Position
l.DeletionAtPosition(3)

l.display()