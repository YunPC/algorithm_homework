import array

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.array = array.array('l', [0]*capacity)
    
    def push(self, value):
        if self.top == self.capacity:
            print('Stack is full!')
        else:
            self.array[self.top] = value
            self.top += 1

    def pop(self):
        if self.top == 0:
            print('Stack is empty!')
        else:
            self.top -= 1
            return self.array[self.top]
    
    def peek(self):
        return self.array[self.top-1]
    
    def is_empty(self):
        return self.top == 0

    def print(self):
        for i in range(self.top-1, -1, -1):
            print(self.array[i])

        print()

stack = Stack(4)
Stack.push(stack, 1)
Stack.push(stack, 2)
Stack.push(stack, 3)

Stack.print(stack)

Stack.pop(stack)

Stack.print(stack)