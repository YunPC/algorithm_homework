class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        if self.head is None:
            return True
        return False

    def prepend(self, value):
        if self.head is None :
            self.head = Node(value, None)
            return
        new_node = Node(value, self.head)
        self.head = new_node

    def append(self, value):
        if self.head is None :
            self.head = Node(value, None)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value, None)

    def set_head(self, index):
        if SinglyLinkedList.is_empty(self):
            print('SSL is empty!')
            return
        node = self.head
        idx = 0
        while node:
            if idx == index:
                self.head = node
                return
            node = node.next
            idx += 1
        print('Invalid index check the size of SSL')

    def access(self, index):
        if SinglyLinkedList.is_empty(self):
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
            SinglyLinkedList.prepend(self, value)
            return
    
        idx = 0
        while node:
            if idx+1 == index:
                new_node = Node(value, node.next)
                node.next = new_node
                return
            node = node.next
            idx += 1
        print('Invalid index check the size of SSL')

    def remove(self, index):
        if SinglyLinkedList.is_empty(self):
            print('SSL is empty!')
            return
        if index == 0:
            self.head = self.head.next
            return
        
        idx = 0
        node = self.head
        while node:
            if idx+1 == index:
                del_node = node.next
                node.next = del_node.next
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


single_linked_list = SinglyLinkedList()

print("----------------------is empty--------------------")
print("this SLL is empty : ", single_linked_list.is_empty())

print("----------------------prepend--------------------")
print('prepend "1-4" into SLL : ', end = '')

for i in range(1, 5):
    single_linked_list.prepend(i)

single_linked_list.print()

print("----------------------append--------------------")
print('append 5 in SSL : ', end = '')

single_linked_list.append(5)

single_linked_list.print()

print("----------------------set head--------------------")
print('set head at -1 (invalid) : ', end = '')
single_linked_list.set_head(-1)

print('set head at third : ', end = '')
single_linked_list.set_head(2)

single_linked_list.print()

print("----------------------access--------------------")
print('Access at -1 (invalid) : ', end = '')
single_linked_list.access(-1)

print('Access at last one : ', end = '')
single_linked_list.access(2)

print("----------------------insert--------------------")

print('Insert -66 at -1 (invalid) : ', end = '')
single_linked_list(-1, 66)

print('Insert 3 at first : ', end = '')
single_linked_list.insert(0, 3)
single_linked_list.print()

print('Insert 6 at last : ', end = '')
single_linked_list.insert(3,6)
single_linked_list.print()

print("----------------------remove--------------------")

print('Remove at -1 (invalid) : ', end = '')
single_linked_list.remove(-1)

print('Remove first value  : ', end = '')
single_linked_list.remove(0)
single_linked_list.print()

print('Remove last value : ', end = '')
single_linked_list.remove(3)
single_linked_list.print()

print('Remove second value : ', end = '')
single_linked_list.remove(1)
single_linked_list.print()