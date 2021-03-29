class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __search(self, value): #private 메소드
        node = self.root
        parent = None
        direction = None
        
        while node:
            if node.value == value:
                break
            elif value < node.value:
                parent = node
                node = node.left
                direction = 'left'
            else:
                parent = node
                node = node.right
                direction = 'right'

        return node, parent, direction
    
    def insert(self, value):
        node, parent, direction = self.__search(value)
        if node:
            return False
        elif direction == 'left':
            parent.left = Node(value, None, None)
        else:
            parent.right = Node(value, None, None)

    def search(self, value):
        node, _, _ = self.__search(value)
        return node

    def remove(self, value):
        pass


bst = BinarySearchTree()
# bst._BinarySearchTree__search(0) 호출 방법(not recommended)
bst.insert(5)
bst.insert(3)
bst.insert(12)

print(bst.search(16))