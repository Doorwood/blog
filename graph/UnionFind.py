class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]

    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)
        if pa==pb:
            return False
        elif pa>pb:
            self.parent[pb] = pa
        else:
            self.parent[pa] = pb
        return True
    def find(self,i):
        if i==self.parent[i]:
            return i
        if self.parent[i]!=i:
            return self.find(self.parent[i])
    def detectCircle(self,edges):
        for e in edges:
            if not self.union(e[0],e[1]):
                return False
        return True
if __name__ == '__main__':
    uf = UnionFind(4)
    edges=[[0,1],[1,2],[2,3]]
    print("no circle") if uf.detectCircle(edges) else print("Has circle")