# 링크드 리스트 큐 import

from DoublyLinkedList import DoublyLinkedList

class LinkedQueue():
    def __init__(self):
        DoublyLinkedList.__init__(self)
        
    def put(self, value):
        DoublyLinkedList.prepend(self, value)

    def get(self):
        value = DoublyLinkedList.access(self, 0)
        DoublyLinkedList.remove(self, 0)
        return value
            
    def peek(self):
        DoublyLinkedList.access(self, 0)

    def print(self):
        DoublyLinkedList.print_reverse(self)


queue = LinkedQueue()
queue.print()

print('----------------------put 1, 2, 3, 4, 5, 6---------------------')
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print('----------------------get 4 times---------------------')
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())

print('----------------------after get 4 times---------------------')
queue.print()

print('----------------------put 4,5,6 ---------------------')
queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print('----------------------get 3 times---------------------')
print(queue.get())
print(queue.get())
print(queue.get())

print('----------------------after get 3 times---------------------')
queue.print()