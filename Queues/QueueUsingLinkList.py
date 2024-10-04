class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enQueue(self,new_data):
        new_node = Node(new_data)
        if self.rear is None:
            self.front=self.rear=new_node
            return
        self.rear.next=new_node
        self.rear=new_node

    def deQueue(self):
        if self.front is None:
            print("Queue Underflow")
            return
        temp=self.front
        self.front=self.front.next
        if self.front is None:
            self.rear=None

    def get_front(self):
        if self.front is None:
            print("Queue is NULL")
            return
        return self.front.data

    def get_rear(self):
        if self.rear is None:
            print("Queue is NULL")
            return
        return self.rear.data

queue=Queue()
queue.enQueue(3)
queue.enQueue(4)
queue.enQueue(6)
queue.enQueue(10)
print(queue.get_rear())
queue.deQueue()
queue.deQueue()
print(queue.get_front())






