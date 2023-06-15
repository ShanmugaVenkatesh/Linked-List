'''
Implemetation of Queue using List

Queue-First In First Out

Operations of Queue:
    Enqueue-Insertion -> occur at Rear End
    Dequeue-Deletion -> occur at Front End

In List->
    Insertion-append()
    Deletion- del queue[0] / pop(0)
'''
def enqueue():
    inp=int(input("Enter the data to be inserted: "))
    queue.append(inp)

def dequeue():
    if len(queue)==0:
        print("Queue is Empty")
    else:
        print(queue[0],"is the poped element")
        del queue[0]
        # or queue.pop(0)

def display():
    if len(queue)==0:
        print("Queue is Empty")
    else:
        for element in queue:
            print(element, end=" ")

queue=list()

while True:
    print("\n1.Enqueue Operation \n2.Dequeue Operation \n3.Display \n4.Exit \n")
    inp=input("Enter the Operations to perform on Queue- ")

    if inp=='1':
        enqueue()
    elif inp=='2':
        dequeue()
    elif inp=='3':
        display()
    else:
        break