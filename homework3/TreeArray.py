import array

class BinaryTree:
    def __init__(self, arr):
        self.array = array.array('l', arr)    
        
    def preorder(self):
        stack = []
        if not array:
            return None
        else:
            visited = [False for _ in range(1, len(self.array)+1)]
            stack.append(self.array[1])
            while stack:
                root = stack.pop() #node
                print(root, end = ' ')
                visited[root] = True
                if root * 2 + 1 < len(self.array) and not visited[root*2+1]: # right
                    stack.append(self.array[root*2+1])
                if root * 2 < len(self.array) and  not visited[root*2]: # left
                    stack.append(self.array[root*2])

    def inorder(self):
        stack = []
        if not array:
            return None
        else:
            visited = [False for _ in range(1, len(self.array)+1)]
            stack.append(self.array[1])
            while stack:
                root = stack[-1]
                if root * 2 < len(self.array) and  not visited[root*2]: # left
                    stack.append(self.array[root*2])
                    continue
                else: # node
                    stack.pop()
                    print(root, end = ' ')
                    visited[root] = True
                if root * 2 + 1 < len(self.array) and not visited[root*2+1]: # right
                    stack.append(self.array[root*2+1])

    def postorder(self):
        stack = []
        if not array:
            return None
        else:
            visited = [False for _ in range(1, len(self.array)+1)]
            stack.append(self.array[1])
            while stack:
                root = stack[-1]
                if root * 2 < len(self.array) and  not visited[root*2]: # left
                    stack.append(self.array[root*2])
                    continue
                if root * 2 + 1 < len(self.array) and not visited[root*2+1]: # right
                    stack.append(self.array[root*2+1])
                else: # node
                    stack.pop()
                    print(root, end = ' ')
                    visited[root] = True
                
                    
                
    
    def bfs(self, value):
        queue = []
        if not array:
            return False
        else:
            visited = [False for _ in range(1, len(self.array)+1)]
            queue.insert(0, self.array[1])
            while queue:
                root = queue[0]
                del queue[0]
                if root == value:
                    return True
                visited[root] = True
                if root * 2 < len(self.array) and  not visited[root*2]: # left
                    queue.append(self.array[root*2])
                if root * 2 + 1 < len(self.array) and not visited[root*2+1]: # right
                    queue.append(self.array[root*2+1])
        return False

    def dfs(self, value):
        stack = []
        if not array:
            return False
        else:
            visited = [False for _ in range(1, len(self.array)+1)]
            stack.append(self.array[1])
            while stack:
                root = stack.pop() #node
                if root == value:
                    return True
                visited[root] = True
                if root * 2 + 1 < len(self.array) and not visited[root*2+1]: # right
                    stack.append(self.array[root*2+1])
                if root * 2 < len(self.array) and  not visited[root*2]: # left
                    stack.append(self.array[root*2])
        return False

arr = [0, 1,2,3,4,5,6,7,8,9,10]
tree = BinaryTree(arr)

tree.bfs(11)
