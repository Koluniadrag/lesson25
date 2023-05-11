class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return data
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.size()) # 3
print(q.dequeue()) # 1
print(q.dequeue()) # 2
print(q.dequeue()) # 3
print(q.is_empty()) # True
