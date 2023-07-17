from collections import deque
from math import inf


class Graph:
    def __init__(self, n):
        self.matrix = [[0] * n for i in range(n)]
        self.edges = []

    def addEdge(self, src, dst, weight):
        self.matrix[src][dst] = weight
        self.edges.append([src,dst,weight])

    def bfs(self, src):
        visited = set()
        visited.add(src)
        queue = deque([src])
        n = len(self.matrix)
        ans = []
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            for i in range(n):
                if self.matrix[cur][i] > 0 and i not in visited:
                    queue.append(i)
                    visited.add(i)
        return ans

    def dfs(self, src):
        visited = set()
        visited.add(src)
        stack = [src]
        n = len(self.matrix)
        ans = []
        while stack:
            cur = stack.pop()
            ans.append(cur)
            for i in range(n):
                if self.matrix[cur][i] > 0 and i not in visited:
                    stack.append(i)
                    visited.add(i)
        return ans

    def dijkstra(self, src):

        n = len(self.matrix)
        spt = [False] * n
        dis = [inf] * n
        dis[src] = 0

        def findMinest(spt, dis):
            minV = inf
            minIdx = -1
            for i in range(len(dis)):
                if not spt[i]:
                    if dis[i] < minV:
                        minIdx = i
                        minV = dis[i]
            return minIdx

        for i in range(n):
            minIdx = findMinest(spt, dis)
            if minIdx == -1:
                break
            spt[minIdx] = True
            for i in range(n):
                if not spt[i] and self.matrix[minIdx][i] > 0:
                    if dis[minIdx] + self.matrix[minIdx][i] < dis[i]:
                        dis[i] = dis[minIdx] + self.matrix[minIdx][i]
        for i in range(n):
            print("shortest to " + str(i) + " " + str(dis[i]))
    def bellmanford(self,src):
        n=len(self.matrix)
        dis = [inf]*n
        dis[src]=0
        for i in range(1,n):
            for s,d,w in self.edges:
                if dis[s]!=inf and dis[s]+w<dis[d]:
                    dis[d]=dis[s]+w
        for s,d,w in self.edges:
            if dis[s]+w<dis[d]:
                raise Exception("Ngative circle!")

        for i in range(n):
            print("shortest to " + str(i) + " " + str(dis[i]))



if __name__ == '__main__':
    # 1->2->3
    # 2->4->3
    graph = Graph(5)
    graph.addEdge(0, 2, 1)
    graph.addEdge(0, 1, 1)
    graph.addEdge(1, 4, 1)
    graph.addEdge(0, 3, 1)
    graph.addEdge(3, 4, -1)
    print(graph.dfs(0))
    print(graph.bfs(0))
    graph.bellmanford(0)
