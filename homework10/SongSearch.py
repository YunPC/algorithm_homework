class Node:
    def __init__(self, value=None):
        self.value = value
        self.child = dict()

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, value:str):
        node = self.root
        for c in value:
            if c not in node.child: # There is no child
                new_node = Node(c)
                node.child[c] = new_node
                node = new_node
            else:
                node = node.child[c]
        node.child['*'] = None
    
    def print(self):
        node = self.root
        queue = []
        queue.append(node)
        while queue:
            root = queue[0]
            del queue[0]

            if root.value is not None:
                print(root.value, end = " ")

            if  '*' in root.child:
                print('*')
                continue

            for node in root.child.values():
                queue.append(node)


trie = Trie()
trie.add('frodo')
trie.add('front')
trie.add('frost')
trie.add('frozen')

trie.print()
   