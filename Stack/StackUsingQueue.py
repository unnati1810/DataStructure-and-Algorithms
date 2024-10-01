# Program to implement a stack using
# two queue
from _collections import deque


class Stack:

    def __init__(self):

        # Two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        # if no elements are there in q1
        if self.is_empty():
            return "Stack is empty"
        # Leave one element in q1 and push others in q2
        while(len(self.q1) > 1):
            self.q2.append(self.q1.popleft())
        popped_element=self.q1.popleft()


        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1
        return popped_element

    def top(self):
        # if no elements are there in q1
        if self.is_empty():
            return "Stack is empty"
        # Leave one element in q1 and push others in q2
        while(len(self.q1) > 1):
            self.q2.append(self.q1.popleft())

        # Pop the only left element from q1 to q2
        top = self.q1[0]
        self.q2.append(self.q1.popleft())

        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

        return top

    def is_empty(self):
        return len(self.q1)==0


# Driver Code
if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.top())  # Output: 30
    print(stack.pop())  # Output: 30
    print(stack.pop())  # Output: 20
    print(stack.is_empty())  # Output: False
    print(stack.pop())  # Output: 10
    print(stack.is_empty())  # Output: True


