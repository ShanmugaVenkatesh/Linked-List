'''
Implementation of Stack using Linkedlist
Push- Insertion at the begining
Pop- Deletion from begining
'''

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
class Stack:
    def __init__(self):
        self.head=None

    # Insertion at the begining
    def push(self): 
        x=int(input("Enter the element to be inserted: "))
        new=Node(x)
        if self.head==None:
            self.head=new
        else:
            temp=self.head
            self.head=new
            new.next=temp

    # Deletion at the begining
    def pop(self):
        if self.head==None:
            print("Stack is Empty")
        else:
            temp=self.head
            print(temp.data,"is the popped element")
            self.head=temp.next
            temp.next=None
            

    def display(self):
        if self.head==None:
            print("Stack is Empty")
        else:
            temp=self.head
            while temp.next!=None:
                print(temp.data)
                temp=temp.next
            print(temp.data)


l=Stack()

while True:
    print("\n1.Push Operation \n2.Pop Operation \n3.Display \n4.Exit \n")
    inp=input("Enter the Operations to perform on Stack- ")
    if inp=='1':
        l.push()
    elif inp=='2':
        l.pop()
    elif inp=='3':
        l.display()
    else:
        break
