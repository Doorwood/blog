class Graph:
    def __init__(self,n) -> None:
        self.graph = []
        self.n = n
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def bellmanFord(self,source):
        distance = [float("Inf")]*self.n
        distance[source] = 0
        for i in range(self.n-1):
            for edge in self.graph:
                if distance[edge[0]]+edge[2]<distance[edge[1]]:
                    distance[edge[1]]=distance[edge[0]]+edge[2]
        print(f"Source is {source}")
        for i in range(self.n):
            print(f"Distance to {i} is {distance[i]}")
        # Detect negative circle in graph
        for edge in self.graph:
            if distance[edge[0]]+edge[2]<distance[edge[1]]:
                print("Exist negative circle!")
                break

if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    # function call
    g.bellmanFord(0)
