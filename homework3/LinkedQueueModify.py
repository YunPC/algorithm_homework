class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedQueue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def put(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            new_node = Node(value, self.head, None)
            self.head.prev = new_node
            self.head = new_node
            
    def get(self):
        value = LinkedQueue.access(self, 0)
        LinkedQueue.remove(self, 0)
        return value

    def peek(self, index):
        if LinkedQueue.is_empty(self):
            return None
        else:
            node = self.head
            idx = 0
            while node:
                if idx == index:
                    return node.value
                node = node.next
                idx += 1

    def access(self, index):
        if LinkedQueue.is_empty(self):
            print('Queue is empty!')
        else:
            node = self.head
            idx = 0
            while node:
                if idx == index:
                    return node.value
                node = node.next
                idx += 1

    def remove(self, index):
        if LinkedQueue.is_empty(self):
            print('Queue is empty!')
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            idx = 0
            node = self.head
            while node:
                if idx+1 == index:
                    del_node = node.next
                    node.next = del_node.next
                    if del_node.next is not None:
                        del_node.next.prev = node
                    else:
                        self.tail = node
                    return
                node = node.next
                idx += 1

    def print(self):
        node = self.tail
        while node:
            print(node.value, end = ' ')
            node = node.prev
        print()


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