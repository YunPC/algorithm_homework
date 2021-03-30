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
            return

        new_node = Node(value, self.head, None)
        self.head.prev = new_node
        self.head = new_node
            

    def append(self, value):
        if self.head is None :
            self.head = Node(value, None, None)
            self.tail = self.head
            return
        
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value, None, node)
        self.tail = node.next

    def set_head(self, index):
        if DoublyLinkedList.is_empty(self):
            print('SSL is empty!')
            return
        
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
            return
        
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
            return
        
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
            return
        
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
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
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


ddl = DoublyLinkedList()

print("----------------------is empty--------------------")
print('DDL is empty : ' , ddl.is_empty())

print("----------------------prepend--------------------")
print('prepend "1-4" into DLL : ', end = '')

for i in range(1, 5):
    ddl.prepend(i)

ddl.print()
print("this DDL is empty : ", ddl.is_empty())

print("----------------------append--------------------")
print('append 5 in SSL : ', end = '')

ddl.append(5)

ddl.print()
print("----------------------set head--------------------")
print('set head at -1 (invalid) : ', end = '')
ddl.set_head(-1)

print('set head at third : ', end = '')
ddl.set_head(2)
ddl.print()
print("----------------------set tail--------------------")
print('set tail at -1 (invalid) : ', end = '')
ddl.set_tail(-1)

print('set tail at second one : ', end = '')
ddl.set_tail(1)
ddl.print()
print("----------------------access--------------------")
print('Access at -1 (invalid) : ', end = '')
ddl.access(-1)

print('Access at last one : ', end = '')
print(ddl.access(1))

print("----------------------insert--------------------")

print('Insert -66 at -1 (invalid) : ', end = '')
ddl.insert(-1, 66)

print('Insert 3 at first : ', end = '')
ddl.insert(0, 3)
ddl.print()
print('Insert 6 at last : ', end = '')
ddl.insert(3, 6)
ddl.print()
print("----------------------remove--------------------")

print('Remove at -1 (invalid) : ', end = '')
ddl.remove(-1)

print('Remove first value  : ', end = '')
ddl.remove(0)
ddl.print()
print('Remove last value : ', end = '')
ddl.remove(2)
ddl.print()
print("----------------------print reverse--------------------")
print('print reverse : ', end = '')
ddl.print_reverse()