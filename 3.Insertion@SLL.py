class SingleLinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        if temp is None:
            print("Linked List is empty")
        else:
            while temp:
                print(temp.data)
                temp=temp.next
    
    # Insertion At the Begining
    def InsertionAtBegining(self,other):
        other.next=self.head
        self.head=other

    # Insertion at the End
    def InsertionAtEnd(self,other):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=other

    # Insertion at the specific position
    def InsertionAtPosition(self,other,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        other.next=prev.next
        prev.next=other

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



l=SingleLinkedList()

n1=Node(10)

l.head=n1
 
n2=Node(20)

n1.next=n2

n3=Node(30)
n2.next=n3

# Insertion at the begining
n0=Node(5)
l.InsertionAtBegining(n0)

# Insertion at the end
n7=Node(7)
l.InsertionAtEnd(n7)

# Insertion at the specific position
n9=Node(1000)
l.InsertionAtPosition(n9,5)

l.display()