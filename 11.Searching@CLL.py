class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def Search(self,value):
        temp=self.head
        count=1
        flag=0
        while temp.next!=self.head:
            if temp.data==value:
                flag=1
                break
            else:
                temp=temp.next
                count=count+1
        else:                       # For last node data to be printed
            if temp.data==value:
                flag=1
        if flag==1:
            print(f"{value} is present in Node {count}")
        else:
            print(f"{value} is not present in Circular Linked List ")

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

l=CircularLinkedList()

n1=Node(10)

l.head=n1
l.tail=n1

n2=Node(20)
l.tail.next=n2  
l.tail=n2         

n3=Node(30)
l.tail.next=n3
l.tail=n3

n4=Node(40)
l.tail.next=n4
l.tail=n4

l.tail.next=l.head

l.Search(40)