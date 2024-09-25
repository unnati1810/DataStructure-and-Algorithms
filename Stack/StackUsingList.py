stack=[]

def push(item):
    stack.append(item)
    return stack

def pop():
    if is_empty():
        return "Stack is empty"
    return stack.pop()

def peek():
    if is_empty():
        print("Cannot read first element, stack is empty")
    return stack[-1]

def is_empty():
    return len(stack)==0

def size():
    return len(stack)

def display():
    print("Below are the elements present in stack",stack)

if __name__ == "__main__":
    # Push elements onto the stack
    push(10)
    push(20)
    push(30)
    push(40)
    push(50)
    push(60)

    # Display stack
    display()

    # Peek at the top element
    print(f'Top element: {peek()}')

    # Pop an element
    print(f'Popped element: {pop()}')

    # Check if the stack is empty
    print(f'Is stack empty? {is_empty()}')

    # Display stack size
    print(f'Stack size: {size()}')

    # Display stack after pop
    display()