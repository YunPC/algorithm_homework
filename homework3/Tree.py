import array

class BinaryTree:
    def __init__(self, arr):
        self.array = array.array('l', arr)    

    def preorder(self):
        s = ''
        def recursive(index):
            if index >= len(self.array): # 종료조건
                return

            s += self.array[index] + ' '
            recursive(2*index + 1) # 재귀호출
            recursive(2*index + 2) # 재귀호출
        recursive(0)
        print(s)

    def inorder(self):
        s = ''
        def recursive(index):
            if index >= len(self.array): # 종료조건
                return

            recursive(2*index + 1) # 재귀호출
            s += self.array[index] + ' '
            recursive(2*index + 2) # 재귀호출
        recursive(0)
        print(s)

    def postorder(self):
        s = ''
        def recursive(index):
            if index >= len(self.array): # 종료조건
                return

            recursive(2*index + 1) # 재귀호출
            recursive(2*index + 2) # 재귀호출
            s += self.array[index] + ' '

        recursive(0)
        print(s)
    
    def bfs(self, value):
        for el in self.array:
            if el == value:
                return True
        return False

    def dfs(self, value):
        s = ''
        isFound = False
        def recursive(index):
            nonlocal isFound

            if index >= len(self.array): # 종료조건
                return
            if isFound is True:
                return
            if value == self.array[index]:
                ifFound = True
                return

            s += self.array[index] + ' '
            recursive(2*index + 1) # 재귀호출
            recursive(2*index + 2) # 재귀호출
        recursive(0)
        
        return isFound