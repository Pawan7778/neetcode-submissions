class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        self.root_num = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    def find(self, k):
        while k != self.par[k]:
            self.par[k] = self.par[self.par[k]]
            k = self.par[k]
        return k
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.rank[root_a] < self.rank[root_b]:
            self.par[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.par[root_b] = self.par[root_a]
        else:
            self.par[root_b] = root_a
            self.rank[root_a] += 1
        self.root_num -= 1
        return True
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for u,v in edges:
            if not uf.union(u, v):
                return False
        return uf.root_num == 1
        