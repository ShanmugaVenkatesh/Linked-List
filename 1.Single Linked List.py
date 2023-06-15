class SingleLinkedList:
    def __init__(self):
        self.head=None

    # Displaying the Linked List
    def display(self):
        temp=self.head
        if temp is None:
            print("Linked List is empty")
        else:
            while temp:
                print(temp.data)
                temp=temp.next
    

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


# creating a head
l=SingleLinkedList()

# Creating a node n1 by passing data-10 and making the address part/next -null
n1=Node(10)

# Linking the head and node n1 (passing the address of the n1 to the head as data)
l.head=n1 # Making the head to point towards node n1

# Creating a node n2 with data-20 
n2=Node(20)
# Linking the address part(next) of n1 with the address of n2
n1.next=n2

n3=Node(30)
n2.next=n3

# Displaying the Linked list
l.display()