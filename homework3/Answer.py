import DoublyLinkedList

class ComposedLinkedQueue: #1. Compostion
    def __init__(self):
        self.dll = DoublyLinkedList() # Composition

    def put(self, value):
        return self.dll.append(value)

    def get(self):
        value = self.dll.access(0)
        if value is not None:
            self.dll.remove(0)
        return value

    def peek(self):
        return self.dll.access(0)

    def print(self):
        self.dll.print()

class DerivedLinkedQueue(DoublyLinkedList): # 상속에 의한 구현(Inheritance)
    def __init__(self):
        super().__init__()

    def put(self, value):
        self.append(value) #다형성의 의미를 가진다.

    def get(self):
        value = self.accesss(0)
        if value is not None:
            self.remove(0)
        return value

    def peek(self):
        return self.access(0)

    def print(self):
        super.print()
        # self.print() 무한 재귀를 발생시킨다.
