"""
front=rear=none --> Queue is Empty
front=rear      --> Queue has one node
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.rear=None
        self.front=None

    # Insertion at the End
    def enqueue(self):
        x=int(input("Enter the data to be inserted: "))
        new=Node(x)
        if self.rear==None and self.front==None:
            self.rear=new
            self.front=new
        elif self.rear==self.front:
            self.rear=new
            self.front.next=new
        else:
            self.rear.next=new
            self.rear=new

    # Deletion at the begining
    def dequeue(self):
        if self.rear==None and self.front==None:
            print("Queue is Empty")
        elif self.rear==self.front:
            print(self.rear.data,"is the poped element")
            self.front=None
            self.rear=None
        else:
            print(self.front.data,"is the poped element")
            temp=self.front
            self.front=self.front.next
            temp.next=None

    def display(self):
        if self.rear==None and self.front==None:
            print("Queue is Empty")
        elif self.rear==self.front:
            print(self.rear.data)
        else:
            temp=self.front
            while self.front!=self.rear:
                print(self.front.data,end=" ")
                self.front=self.front.next
            print(self.front.data)
            self.front=temp

l=Queue()

while True:
    print("\n1.Enqueue Operation \n2.Dequeue Operation \n3.Display \n4.Exit \n")
    inp=input("Enter the Operations to perform on Queue- ")

    if inp=='1':
        l.enqueue()
    elif inp=='2':
        l.dequeue()
    elif inp=='3':
        l.display()
    else:
        break