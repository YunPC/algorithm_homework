class Vertex:
    def __init__(self, value, adj_list=None): #mutable parameter는 기본값으로 초기화를 하면 안된다.
        self.value = value
        if adj_list is None:
            adj_list = []
        self.adj_list = adj_list

class Graph:
    def __init__(self):
        self.verticies = []

    def insert(self, value, adj_list): #adj_list에는 index가 들어가 있다고 가정한다
        v = Vertex(value, adj_list)
        self.verticies.append(v)
        v_ind = len(self.verticies) -1
        for adj_v_ind in v.adj_list:
            self.verticies[adj_v_ind].adj_list.append(v_ind)

    def bfs(self, vert_ind, value):
        queue = []
        queue.append(vert_ind)
        visited = [False] * len(self.verticies)

        while queue:
            v_ind = queue.pop(0)
            v = self.verticies[v_ind]

            if visited[v_ind]:
                continue

            visited[v_ind] = True
            
            if v.value == value:
                return True

            for adj_v_ind in v.adj_list:
                if visited[adj_v_ind] is False:
                    queue.append(adj_v_ind)

        return False

    def dfs(self, vert_ind, value):
        isFound = False # 객체를 다른 애로 바꾸는 것이기 때문에 nonlocal을 사용해야 함
        visited = [False] * len(self.vertices) # 객체가 다른 객체를 가리키게 되는 게 아니므로 nonlocal 할 필요 없음

        def recursive(ind):
            nonlocal isFound
            if visited[ind]:
                return
            
            if isFound:
                return

            visited[ind] = True
            v = self.verticies[ind]
            if v.value == value:
                isFound = True
                return
            
            for adj_v_ind in v.adj_list:
                if visited[adj_v_ind] is False:
                    recursive(adj_v_ind)

        recursive(vert_ind)
        return isFound