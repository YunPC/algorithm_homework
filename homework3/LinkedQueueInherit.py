# 링크드 리스트 큐 상속

class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        if self.head is None:
            return True
        return False

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            new_node = Node(value, self.head, None)
            self.head.prev = new_node
            self.head = new_node
            

    def append(self, value):
        if self.head is None :
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value, None, node)
            self.tail = node.next

    def set_head(self, index):
        if DoublyLinkedList.is_empty(self):
            print('SSL is empty!')
        else:
            node = self.head
            idx = 0
            while node:
                if idx == index:
                    self.head = node
                    node.prev = None
                    return
                node = node.next
                idx += 1
            print('Invalid index check the size of SSL')

    def set_tail(self, index):
        if DoublyLinkedList.is_empty(self):
            print('SSL is empty!')
        else:
            node = self.head
            idx = 0
            while node:
                if idx == index:
                    self.tail = node
                    self.tail.next = None
                    return
                node = node.next
                idx += 1
            print('Invalid index check the size of SSL')

    def access(self, index):
        if DoublyLinkedList.is_empty(self):
            print('SSL is empty!')
        else:
            node = self.head
            idx = 0
            while node:
                if idx == index:
                    return node.value
                node = node.next
                idx += 1
            print('Invalid index check the size of SSL')

    def insert(self, index, value):
        node = self.head
        if index == 0:
            DoublyLinkedList.prepend(self, value)
        else:
            idx = 0
            while node:
                if idx+1 == index:
                    new_node = Node(value, node.next, node)
                    new_node.next = node.next
                    new_node.prev = node
                    node.next = new_node
                    if new_node.next is not None:
                        new_node.next.prev = new_node
                    else:
                        self.tail = new_node
                    return
                node = node.next
                idx += 1
            print('Invalid index check the size of SSL')

    def remove(self, index):
        if DoublyLinkedList.is_empty(self):
            print('SSL is empty!')
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
            print('Invalid index check the size of SSL')
        

    def print(self):
        node = self.head
        while node:
            print(node.value, end = ' ')
            node = node.next
        print()

    def print_reverse(self):
        node = self.tail
        while node:
            print(node.value, end = ' ')
            node = node.prev
        print()


class LinkedQueue(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        
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
