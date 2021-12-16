# Arshia_yousefinezhad
# University Project
# In The name of God
class Stack:
    class Node:
        def __init__(self, data, after):
            self._data = data
            self._next = after
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def add2first(self, p):
        node = self.Node(p, None)
        if self.is_empty():
            self._head = node
        else:
            node._next = self._head
            self._head = node
        self._size += 1

    def removefirst(self):
        tmp = self._head
        if self.is_empty():
            return None
        else:
            if self._size == 1:
                self._head = None
                self._size -= 1
                return tmp._data
            else:
                self._head = self._head._next
                self._size -= 1
                return tmp._data

    def top(self):
        if self.is_empty():
            return None
        return self._head._data

    def show(self):
        tmp = self._head
        while tmp != None:
            print(tmp._data, end='  -> ')
            tmp=tmp._next
        print()
class Queue:
    class Node:
        def __init__(self, data, after):
            self._data = data
            self._next = after
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def add2last(self, p):
        node = self.Node(p, None)
        if self.is_empty():
            self._head = node
        else:
            tmp = self._head
            while tmp._next != None:
                tmp = tmp._next
            tmp._next = node
        self._size += 1

    def removefirst(self):
        tmp = self._head
        if self.is_empty():
            return None
        else:
            if self._size == 1:
                self._head = None
                self._size -= 1
                return tmp._data
            else:
                self._head = self._head._next
                self._size -= 1
                return tmp._data

    def top(self):
        if self.is_empty():
            return None
        return self._head._data

    def show(self):
        tmp = self._head
        while tmp != None:
            print('[',tmp._data.ver, ',', tmp._data.Edge,']',end='  -> ')
            tmp=tmp._next
        print()
class Graph:
    def __init__(self, vertex):
        self.adj = []
        self.parent = []
        for i in range(vertex):
            self.adj.append([0 for i in range(vertex)])
        self.v = vertex

    def addEdge(self, u, v, e):
        self.parent.append([e, v, u])
        self.adj[u][v] = e

    def addVertex(self):
        old = self.adj
        self.v += 1
        self.adj = []
        for v in range(self.v):
            self.adj.append([0 for v in range(self.v)])
        for j in range(self.v-1):
            for i in range(self.v):
                if i == self.v - 1:
                    self.adj[j][i] = 0
                else:
                    self.adj[j][i] = old[j][i]

    def all_Edge(self):
        count = 0
        for i in self.adj:
            for j in i:
                if j != 0:
                    count += 1
        print("all_Edge: ", count)

    def out_vertex(self, u):
        count = 0
        for i in self.adj[u]:
            if i != 0:
                count += 1
        print('out_vertex: ',count)

    def in_vertex(self, u):
        count = 0
        for i in range(self.v):
            if self.adj[i][u] != 0:
                count += 1
        print('in_vertex: ',count)

    def show(self):
        for i in self.adj:
            print(i)

    def BFS(self, v):
        visited = [False] * len(self.adj)
        queue = Queue()
        queue.add2last(v)
        visited[v] = True
        while queue._size != 0:
            v = queue.removefirst()
            print(v, end='->')
            for n in self.adj[v]:
                if n != 0:
                    if visited[g.adj[v].index(n)] is False:
                        queue.add2last(g.adj[v].index(n))
                        visited[g.adj[v].index(n)] = True

    def DFS(self, s):
        visited = [False] * (len(self.adj))
        stack = Stack()   # probing
        stack.add2first(s)
        visited[s] = True
        print(s, end='->')
        while stack._size != 0:
            for i in range(self.v):
                if visited[i] is False and self.adj[s][i] > 0:
                    a = i
                    stack.add2first(a)
                    visited[a] = True
                    print(a, end='->')
                    s = stack.top()
                    break
                if i == len(self.adj[s])-1:
                    s = stack.top()
                    stack.removefirst()
        print()

    def kruskal(self):
        lst = []
        self.parent.sort()
        visited = [False] * self.v
        for i in range(len(self.parent)):
            if visited[self.parent[i][1]] is False or visited[self.parent[i][2]] is False:
                if visited[self.parent[i][1]] is False:
                    visited[self.parent[i][1]] = True
                if visited[self.parent[i][2]] is False:
                    visited[self.parent[i][2]] = True
                lst.append(self.parent[i])
        print("vertex", "\t\t", "Distance")
        for p in range(len(lst)):
            print(lst[p][1], '__', lst[p][2], "\t\t\t", lst[p][0])

    def dijkstra(self, ver):
        key = [100000] * self.v
        key[ver] = 0
        Visited = [False] * self.v
        for cout in range(self.v):
            minimum = 1000
            for t in range(self.v):
                if key[t] < minimum and Visited[t] is False:
                    minimum = key[t]
                    mini_index = t
            u = mini_index
            Visited[u] = True
            for v in range(self.v):
                if self.adj[u][v] != 0 and Visited[v] is False and key[v] > key[u] + self.adj[u][v]:
                    key[v] = key[u] + self.adj[u][v]

        print("Vertex \tDistance from", ver)
        for node in range(self.v):
            print(node, "\t\t", key[node])

if __name__ == '__main__':
    file = open('graph.txt', 'r')
    vertex = file.readline()
    Edge = file.readline()
    g = Graph(int(vertex))
    lst = []
    for i in range(int(Edge)):
        m = file.readline()
        r = m.split()
        lst.append(r)
    for t in lst:
        v = t[0]
        u = t[1]
        e = t[2]
        g.addEdge(int(v), int(u), int(e))
    file.close()

    g.show()
    print()
    g.in_vertex(1)
    g.out_vertex(2)
    g.all_Edge()
    print()
    print("BFS(0)", end=': ')
    g.BFS(0)
    print()
    print("DFS(0)", end=': ')
    g.DFS(0)
    print()
    print("------kruskal------")
    g.kruskal()
    print()
    print("------dijkstra------")
    g.dijkstra(1)
