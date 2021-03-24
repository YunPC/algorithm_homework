import array

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.size == self.capacity:
            print('Queue is full!')
        else:
            self.array[self.rear] = value
            self.rear = (self.rear+1) % self.capacity
            self.size += 1

    def get(self):
        if self.size == 0:
            print('Queue is empty')
        else:
            value = self.array[self.front]
            self.front = (self.front+1) % self.capacity
            self.size -= 1
            return value

    def peek(self):
        if self.size == 0:
            print('Queue is empty')
        else:
            return self.array[self.front]

    def print(self):
        idx = self.front
        for _ in range(self.size):
            print(self.array[idx] , end = ' ')
            idx += 1
            if idx == self.capacity:
                idx = 0
        print()


queue = CircularQueue(5)
queue.print()

queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
queue.print()

queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())
queue.print()