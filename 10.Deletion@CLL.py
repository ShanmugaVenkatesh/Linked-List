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

    # Deletion At Begining
    def DeletionAtBegining(self):
        if self.head==None:
            print("No node is present in Circular linked list")
        # Checking whether CLL consist of one node
        elif self.head==self.tail:
            self.head=None   
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.tail.next=self.head             

    # Deletion At End
    def DeletionAtEnd(self):
        if self.head==None:
            print("No node is present in Circular linked list")
        # Checking whether CLL consist of one node
        elif self.head==self.tail:
            self.head=None  
        else:
            temp=self.head.next
            prev=self.head
            while temp.next != self.head:
                temp=temp.next
                prev=prev.next
            prev.next=self.head
            self.tail.next=None
            self.tail=prev 
        '''
            temp=self.head
            while temp.next!=self.tail:
                temp=temp.next
            self.tail=None
            self.tail=temp
            self.tail.next=self.head
        ''' 

    # Deletion At specific Position
    def DeletionAtPosition(self,pos):
        if self.head==None:
            print("No node is present in Circular linked list")
        # Checking whether CLL consist of one node
        elif self.head==self.tail:
            self.head=None 
        else:
            temp=self.head.next
            prev=self.head
            for i in range(1,pos-1):
                temp=temp.next
                prev=prev.next
            prev.next=temp.next
            temp.next=None        

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

# Deletion At Begining
l.DeletionAtBegining()

# Deletion At End
l.DeletionAtEnd()

# Deletion At specific Position
l.DeletionAtPosition(3)

l.display()