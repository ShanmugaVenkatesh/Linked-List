class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def display(self):
        temp=self.head
        if temp is None:
            print("Circular Linked List is Empty")
        else:
            print(temp.data)
            while temp.next != self.head:
                temp=temp.next
                print(temp.data)

    # Insertion At the Begining
    def InsertionAtBegining(self,X):
        # Creating a node inside the function
        new=Node(X)
        temp=self.head
        # If the Circular Linked list is empty, then new node gets added and its address/link part will be its own address
        if temp is None:        
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            temp=self.head
            self.head=new
            new.next=temp
            self.tail.next=self.head

    # Insertion At the End
    def InsertionAtEnd(self,X):
        new=Node(X)
        temp=self.head
        if temp is None:        
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
           self.tail.next=new
           self.tail=new
           self.tail.next=self.head

    # Insertion At the specific Position
    def InsertionAtPosition(self,X,pos):
        new=Node(X)
        temp=self.head
        if temp is None:        
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            if pos==1:
                self.InsertAtBegining(X)
            else:
                for i in range(1,pos-1):
                    temp=temp.next
                new.next=temp.next
            temp.next=new        

l=CircularLinkedList()

n1=Node(100)
l.tail=n1
l.head=n1

n2=Node(200)
l.tail.next=n2          
l.tail=n2

n3=Node(300)
l.tail.next=n3
l.tail=n3

n4=Node(400)
l.tail.next=n4
l.tail=n4

n5=Node(500)
l.tail.next=n5
l.tail=n5

l.tail.next=l.head

# Insertion At the Begining
l.InsertionAtBegining(60)

# Insertion At the End
l.InsertionAtEnd(900)

# Insertion At the specific Position
l.InsertionAtPosition(101,6)

l.display()