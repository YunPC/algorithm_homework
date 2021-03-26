class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value, self.head)
        else:
            curr = self.head
            while curr.next:
                if curr.next == self.head:
                    break
                curr = curr.next
            curr.next = Node(value, self.head)
            

    def print(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

queue = CircularLinkedList()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

queue.print()
