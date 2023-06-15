class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        if temp is None:
            print("Double LinkedList is Empty")
        else:
            while temp:
                print(temp.data)
                temp=temp.next

    # Deletion at Begining
    def DeletionAtBegining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None

    # Deletion at End
    def DeletionAtEnd(self):
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
            before=before.next
        before.next=None
        temp.prev=None

    # Deletion at specific Position
    def DeletionAtPosition(self,pos):
        temp=self.head.next
        before=self.head
        for i in range(1,pos-1):
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp.next.prev=before
        temp.next=None
        temp.prev=None

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

l=DoubleLinkedList()

n1=Node(10)
l.head=n1

n2=Node(20)
n1.next=n2
n2.prev=n1

n3=Node(30)
n2.next=n3
n3.prev=n2

n4=Node(570)
n4.prev=n3
n3.next=n4

n5=Node(99)
n5.prev=n4
n4.next=n5

# Deletion at Begining
l.DeletionAtBegining()

# Deletion at End
l.DeletionAtEnd()

# Deletion at specific Position
l.DeletionAtPosition(3)

l.display()