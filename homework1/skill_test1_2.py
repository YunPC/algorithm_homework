import math

def solution(n):
    
    root = math.sqrt(n)

    if root == math.floor(root):
        return math.pow(root+1, 2)
    else:
        return -1
    