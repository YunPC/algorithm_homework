import array

class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.front == self.capacity:
            print('Can\'t put!')
        else:
            if self.rear == self.capacity:
                print('Queue is Already Used!')
            else :
                self.array[self.rear] = value
                self.rear += 1

    def get(self):
        if self.front == self.rear:
            return None
        elif self.front == self.capacity:
            return None
        else:
            value = self.array[self.front]
            self.front += 1
            return value
            
    def peek(self):
        if self.front == self.rear:
            print('Queue is empty')
        elif self.rear == capacity:
            print('Already Used all')
        else:
            return self.array[self.rear]

    def print(self):
        if self.front == self.rear:
            print('Queue is empty')
        for i in range(self.front, self.rear):
            print(self.array[i], end = ' ')
        print()

    
queue = LinearQueue(5)
queue.print()

print('----------------------put 1, 2, 3---------------------')
queue.put(1)
queue.put(2)
queue.put(3)

queue.print()

print('----------------------get 4 times---------------------')
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
queue.print()

print('----------------------put 4, 5, 6---------------------')
queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print('----------------------get 3 times---------------------')
print(queue.get())
print(queue.get())
print(queue.get())
queue.print()