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

    # Insert at the begining
    def InsertAtBegining(self,other):
        temp=self.head
        self.head=other
        other.next=temp
        temp.prev=other

    # Insert at the End
    def InsertAtEnd(self,other):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=other
        other.prev=temp

    # Insert at the specific Position
    def InsertAtPosition(self,other,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=other
        other.prev=prev
        other.next=temp
        temp.prev=other

    # or another way for Insertion at the specific position
    ''' def InsertionAtPosition(self,other,pos):
            temp=self.head()
            for i in range(1,pos-1):
                temp=temp.next
            other.prev=temp
            other.next=temp.next
            temp.next.prev=other
            temp.next=other
    '''

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
# Insert at the begining
l.InsertAtBegining(n4)

n5=Node(500)
# Insert at the End
l.InsertAtEnd(n5)

n6=Node(666)
# Insert at the specific Position
l.InsertAtPosition(n6,3)

l.display()