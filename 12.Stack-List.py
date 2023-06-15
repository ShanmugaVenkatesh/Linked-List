def push():
    x=int(input("Enter the element to be inserted: "))
    if stack.count==0:
        stack.append(x)
    else:
        stack.insert(0,x)

def pop():
    if stack.count==0:
        print("Stack is Empty")
    else:
        print(stack[0],"is deleted")
        del stack[0]

def display():
    if stack.count==0:
        print("Stack is Empty")
    else:
        for element in stack:
            print(element)

stack=list()

while True:
    print("\n1.Push Operation \n2.Pop Operation \n3.Display \n4.Exit \n")
    inp=input("Enter the Operations to perform on Stack- ")

    if inp=='1':
        push()
    elif inp=='2':
        pop()
    elif inp=='3':
        display()
    else:
        break
