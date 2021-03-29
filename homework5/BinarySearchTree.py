class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # Ref: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/40885162
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __search(self, value):
        node = self.root
        parent = None
        direction = None

        while node:
            if node.value == value:
                break
            elif value < node.value:
                parent = node
                direction = 'left'
                node = node.left
            else:
                parent = node
                direction = 'right'
                node = node.right

        return parent, node, direction

    def __connect(self, direction, parent, child):
        if direction == 'left':
            parent.left = child
        elif direction == 'right':
            parent.right = child
        else:
            return

    def insert(self, value):
        parent, node, direction = self.__search(value)

        if parent is None:
            self.root = Node(value)
            return True
        
        if node is not None:
            return False

        if direction == 'left':
            parent.left = Node(value)
        else:
            parent.right = Node(value)

        return True

    def search(self, value):
        _, node, _ = self.__search(value)
        return node
    
    def remove(self, value):
        parent, node, direction = self.__search(value)
        
        if node.left is None and node.right is None: #leaf node
            self.__connect(direction, parent, None)
        elif node.left is not None and node.right is not None: #both child node
            #find new node
            new_node_parent = node
            new_node = node.right
            while new_node.left:
                new_node_parent = new_node
                new_node = new_node.left

            #set new connect
            new_node.left = node.left # left side
            self.__connect(direction, parent, new_node) # parent-child

            # Exception case : 대체 노드의 오른쪽에 자식이 남아있는 경우 대체노드의 부모의 왼쪽에 붙여줘야 한다.
            if new_node_parent != node and new_node.right: 
                new_node_parent.left = new_node.right
                new_node.right = node.right
            # Exception case : 대체 노드가 자식이 없고 지우고자 하는 노드가 대체 노드의 부모일 때
            elif new_node.right is None and node.right == new_node:
                new_node.right = None
            # Exception case : 대체 노드가 자식이 없고 지우고자 하는 노드가 대체 노드의 부모가 아닐 때
            elif new_node.right is None and node.right != new_node:
                new_node_parent.left = None
                new_node.right = node.right 
            # Exception case : 루트를 지우는 경우 루트값을 새로 갱신해야 한다.
            if parent is None:
                self.root = new_node
        else: # one child node
            child = node.left if node.left else node.right
            self.__connect(direction, parent, child)
                
                



# bst._BinarySearchTree__search(0) 호출 방법(not recommended)
bst = BinarySearchTree()

import random
x = list(range(20))
random.shuffle(x)
for el in x:
    bst.insert(el)
bst.root.display()

print('------------------remove 6----------------------')
bst.remove(6)
bst.root.display()

print('------------------remove 10----------------------')
bst.remove(10)
bst.root.display()