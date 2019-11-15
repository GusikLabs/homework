
import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)]

    def printMST(self, parent):
        print ("Алгоритм Прима\n")
    
        for i in range(1, self.V):
            print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ])

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def prima_Algoritm(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
        self.printMST(parent)


g = Graph(8)
g.graph = [ [0, 0, 7,3, 1, 6, 0, 0],
            [0, 0, 2, 9, 0, 9, 0, 0],
            [7, 2, 0, 0, 0, 7, 0, 4],
            [3, 9, 0, 0, 5, 0,10, 0],
            [1, 0, 0, 5, 0, 4, 1, 4],
            [6, 9, 7, 0, 4, 0, 8, 7],
            [0, 0, 0, 10, 1, 8, 0, 5],
            [0, 0, 4, 0, 4, 7, 5, 0]]

g.prima_Algoritm();


from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.V= vertices
        self.graph = []

    def Edge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    def Kruskal_Algorithm(self):
        result =[]
        i = 0
        e = 0
        self.graph =  sorted(self.graph,key=lambda item: item[2])
        parent = [] ; rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V -1 :
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
            if x != y:
                e = e + 1    
                result.append([u,v,w])
                self.union(parent, rank, x, y)            
        print ("Алгоритм Крускала\n")
        for u,v,weight  in result:
            print ("%d - %d    %d" % (u,v,weight))

g = Graph(8)
g.Edge(0, 2, 6)
g.Edge(0, 3, 2)
g.Edge(0, 3, 2)
g.Edge(1, 2, 2)
g.Edge(1, 5, 1)
g.Edge(2, 5, 9)
g.Edge(1, 6, 9)
g.Edge(3, 4, 9)
g.Edge(3, 5, 6)
g.Edge(4, 5, 7)
g.Edge(4, 7, 10)
g.Edge(5, 7, 6)
g.Edge(6, 7, 2)

g.Kruskal_Algorithm () 
