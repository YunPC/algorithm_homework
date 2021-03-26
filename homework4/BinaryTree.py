class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        stack = []
        if self.root is None:
            return None
        else:
            stack.append(self.root)
            while stack:
                root = stack.pop() #node
                print(root.value, end = ' ')
                if root.right is not None: # right
                    stack.append(root.right)
                if root.left is not None: # left
                    stack.append(root.left)
    
    def inorder(self):
        stack = []
        visited = {}
        if self.root is None:
            return None
        else:
            stack.append(self.root)
            while stack:
                root = stack[-1] #node
                if root.left is not None and visited.get(root.left.value) is None: # left
                    stack.append(root.left)
                    continue
                else:
                    stack.pop()
                    print(root.value, end = ' ')
                    visited[root.value] = True
                if root.right is not None and visited.get(root.right.value) is None: # right
                    stack.append(root.right)
    
    def postorder(self):
        stack = []
        visited = {}
        if self.root is None:
            return None
        else:
            stack.append(self.root)
            while stack:
                root = stack[-1] #node
                if root.left is not None and visited.get(root.left.value) is None: # left
                    stack.append(root.left)
                    continue
                if root.right is not None and visited.get(root.right.value) is None: # right
                    stack.append(root.right)
                else:
                    stack.pop()
                    print(root.value, end = ' ')
                    visited[root.value] = True
                

    def bfs(self, value):
        queue = []
        if not self.root:
            return False
        else:
            visited = {}
            queue.insert(0, self.root)
            while queue:
                root = queue[0]
                del queue[0]
                if root.value == value:
                    return True
                visited[root] = True
                if root.left is not None and visited.get(root.left.value) is None: # left
                    queue.append(root.left)
                    continue
                if root.right is not None and visited.get(root.right.value) is None: # right
                    queue.append(root.right)
        return False
    
    def dfs(self, value):
        return False


arr = [0,1,2,3,4,5,6,7,8,9]

b_tree = BinaryTree(arr)

print('-----------------------preorder-------------------')
b_tree.postorder()
print()

print('-----------------------inorder-------------------')
b_tree.inorder()
print()

print('-----------------------postorder-------------------')
b_tree.postorder()
print()

print('-----------------------bfs-------------------')
print('Find 7 with bfs : ', b_tree.bfs(7))
print('Find 28 with bfs : ', b_tree.bfs(28))

print('-----------------------dfs-------------------')
print('Find 7 with dfs : ', b_tree.bfs(7))
print('Find 28 with dfs : ', b_tree.bfs(28))