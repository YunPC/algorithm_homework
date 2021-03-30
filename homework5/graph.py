class Vertex:
    def __init__(self, value, adj_list=None):
        self.value = value
        if adj_list is None:
            adj_list = []
        self.adj_list = adj_list


class Graph:

    def __init__(self):
        self.vertices = []
        self.index = 0

    def insert(self, value, adj_list):
        self.vertices.append(Vertex(value, adj_list))

    def bfs(self, vert_ind, value):
        visited = {}

        queue = []
        queue.append(vert_ind)
        while queue:
            v = queue.pop(0)
            if visited.get(v) is None:
                print(v, end = ' ')
            visited[v] = True
            if v == value:
                return True
            for vertex in self.vertices:
                if vertex.value == v:
                    for adj_v in vertex.adj_list:
                        if visited.get(adj_v) is None:
                            queue.append(adj_v)
                    break
        return False

    def dfs(self, vert_ind, value):
        visited = {}

        stack = []
        stack.append(vert_ind)
        while stack:
            v = stack.pop()
            if visited.get(v) is None:
                print(v, end = ' ')
            visited[v] = True
            if v == value:
                return True
            for vertex in self.vertices:
                if vertex.value == v:
                    for adj_v in vertex.adj_list:
                        if visited.get(adj_v) is None:
                            stack.append(adj_v)
                            break
                    break
        return False


g = Graph()
g.insert(1, [2, 5])
g.insert(2, [1, 3])
g.insert(3, [2, 4, 5])
g.insert(4, [3, 5])
g.insert(5, [3, 1, 4])

g.bfs(1, 6)
print()
g.dfs(1, 6)