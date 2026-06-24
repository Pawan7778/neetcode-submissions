class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
      
        def union(a, b):
            roota , rootb = find(a), find(b)

            if roota == rootb:
                return False
            parent[roota] = rootb
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False
        
        return True 
