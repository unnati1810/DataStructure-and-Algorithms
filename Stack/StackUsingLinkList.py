
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.count=0

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
        self.count+=1

    def pop(self):
        if self.is_empty():
            print("Stack is empty, can't delete anything")
        else:
            temp=self.head
            self.head=self.head.next
            del temp

    def is_empty(self):
        return self.count==0

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.head.data

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

stack.pop()
stack.pop()

print("Top element is", stack.peek())


