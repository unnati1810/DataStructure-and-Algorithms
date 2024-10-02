

class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def enQueue(self,number):
        self.s1.append(number)

    def deQueue(self):
        if self.is_empty():
            print("Queue is empty")
        while len(self.s1)>1:
            self.s2.append(self.s1.pop())
        popped_element=self.s1.pop()
        self.s1,self.s2=self.s2,self.s1
        return popped_element

    def top(self):
        if self.is_empty():
            print("Queue is empty")
        while len(self.s1)>1:
            self.s2.append(self.s1.pop())
        top=self.s1[0]
        self.s1,self.s2=self.s2,self.s1
        self.s1.append(top)
        return top

    def is_empty(self):
        return len(self.s1)==0

queue=Queue()
queue.enQueue(2)
queue.enQueue(4)
queue.enQueue(6)
queue.enQueue(7)
print(queue.top())
queue.deQueue()
queue.deQueue()
print(queue.top())


