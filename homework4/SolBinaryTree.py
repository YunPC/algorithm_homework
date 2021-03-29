class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2*ind +1
            right = 2*ind +2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def bfs(self, value):
        queue = []
        queue.append(self.root) # put
        
        while queue:
            node = queue.pop(0) # get

            if node.value == value:
                return True
            
            # Truthy, Falsy
            # Truthy : True, 차있는 list, 0이 아닌 숫자(음수 포함), None이 아닌 참조
            # Falsy : False, 비어있는 list, 숫자 0, None인 참조

            # ==, is 
            # == -> 값을 비교해서 같으면 True
            # is -> 동일한 객체인지를 화인해서 같으면 True (id()를 비교하여 확인)
            #       파이썬에서는 id()(= 참조)가 유일하게 객체를 구분하는 수단(주소값은 알 수 없음)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs_recursive(self, value):
        isFound = False

        def recursive(node):
            nonlocal isFound

            if isFound:
                return

            if node is None:
                return False

            if node.value == value:
                isFound = True
                return True
            
            if node.left:
                recursive(node.left)
            
            if node.right:
                recursive(node.right)

        recursive(self.root)

        return isFound

    def dfs_stack(self, value): # better!
        stack = []
        stack.append(self.root) # push

        while stack:
            node = stack.pop() # pop
            
            if node.value == value:
                return True
            
            if node.right:
                stack.append(right)

            if node.left:
                stack.append(left)
        
        return False



        


