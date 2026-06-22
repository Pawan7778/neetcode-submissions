class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.component = n
    def find(self, k):
        if k == self.parent[k]:
            return k
        self.parent[k] = self.find(self.parent[k])
        return self.parent[k]
    def union(self, a, b):
        roota, rootb = self.find(a), self.find(b)
        if roota == rootb:
            return
        if self.rank[roota] < self.rank[rootb]:
            self.parent[roota] = rootb
        elif self.rank[rootb] < self.rank[roota]:
            self.parent[rootb] = roota
        else:
            self.parent[roota] = rootb
            self.rank[rootb] += 1
        self.component -= 1
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.component
        