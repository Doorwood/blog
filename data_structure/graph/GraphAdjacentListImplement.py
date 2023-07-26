import heapq
from collections import deque
from math import inf


class Graph:

    def __init__(self,n):
        self.adjList = [[] for _ in range(n)]
    def addEdge(self,src,dst,weight):
        self.adjList[src].append([weight,dst])
        # heapq.heappush(self.adjList[src],[weight,dst])
    def dfs(self,src):
        stack = [src]
        visited = set()
        visited.add(src)
        ans=[]
        while stack:
            cur = stack.pop()
            ans.append(cur)
            for ne in self.adjList[cur]:
                if ne[1] in visited:
                    continue
                visited.add(ne[1])
                stack.append(ne[1])
        return ans
    def bfs(self,src):
        queue = deque([src])
        visited = set()
        visited.add(src)
        ans=[]
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            for ne in self.adjList[cur]:
                if ne[1] in visited:
                    continue
                visited.add(ne[1])
                queue.append(ne[1])
        return ans
    # Greedy Algorithm
    # Choose the smallest way in each time

    def dijkstra(self,src):
        pq = [] # store current minest node
        pq.append([0,src])
        n = len(self.adjList)
        dis=[inf] * n # record current distance
        dis[src]=0
        while pq:
            cur = heapq.heappop(pq)
            for adj in self.adjList[cur[1]]:
                if dis[cur[1]]+adj[0]<dis[adj[1]]:
                    dis[adj[1]] = dis[cur[1]]+adj[0]
                    heapq.heappush(pq,[dis[adj[1]],adj[1]])
        for i in range(n):
            print("shortest to "+str(i)+" "+str(dis[i]))











if __name__ == '__main__':
    # 1->2->3
    # 2->4->3
    graph = Graph(5)
    graph.addEdge(0,2,1)
    graph.addEdge(0,1,1)
    graph.addEdge(1,4,1)
    graph.addEdge(0,3,1)
    graph.addEdge(3,4,1)
    print(graph.dfs(0))
    print(graph.bfs(0))
    graph.dijkstra(0)
