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
        else:
            new_node = Node(value, self.head)
            self.head = new_node

    def append(self, value):
        if self.head is None :
            self.head = Node(value, None)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value, None)

    def set_head(self, index):
        if SinglyLinkedList.is_empty(self):
            print('SSL is empty!')
        else:
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
            SinglyLinkedList.prepend(self, value)
        else:
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
        if index == 0:
            self.head = self.head.next
        else:
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
print("this SLL is empty : ", SinglyLinkedList.is_empty(single_linked_list))

print("----------------------prepend--------------------")
print('prepend "1-4" into SLL : ', end = '')

for i in range(1, 5):
    SinglyLinkedList.prepend(single_linked_list, i)

SinglyLinkedList.print(single_linked_list)

print("----------------------append--------------------")
print('append 5 in SSL : ', end = '')

SinglyLinkedList.append(single_linked_list, 5)

SinglyLinkedList.print(single_linked_list)

print("----------------------set head--------------------")
print('set head at -1 (invalid) : ', end = '')
SinglyLinkedList.set_head(single_linked_list, -1)

print('set head at third : ', end = '')
SinglyLinkedList.set_head(single_linked_list, 2)

SinglyLinkedList.print(single_linked_list)

print("----------------------access--------------------")
print('Access at -1 (invalid) : ', end = '')
SinglyLinkedList.access(single_linked_list, -1)

print('Access at last one : ', end = '')
print(SinglyLinkedList.access(single_linked_list, 2))

print("----------------------insert--------------------")

print('Insert -66 at -1 (invalid) : ', end = '')
SinglyLinkedList.insert(single_linked_list, -1, 66)

print('Insert 3 at first : ', end = '')
SinglyLinkedList.insert(single_linked_list, 0, 3)
SinglyLinkedList.print(single_linked_list)

print('Insert 6 at last : ', end = '')
SinglyLinkedList.insert(single_linked_list, 3, 6)
SinglyLinkedList.print(single_linked_list)

print("----------------------remove--------------------")

print('Remove at -1 (invalid) : ', end = '')
SinglyLinkedList.remove(single_linked_list, -1)

print('Remove first value  : ', end = '')
SinglyLinkedList.remove(single_linked_list, 0)
SinglyLinkedList.print(single_linked_list)

print('Remove last value : ', end = '')
SinglyLinkedList.remove(single_linked_list, 3)
SinglyLinkedList.print(single_linked_list)

print('Remove second value : ', end = '')
SinglyLinkedList.remove(single_linked_list, 1)
SinglyLinkedList.print(single_linked_list)