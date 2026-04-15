class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        res = 0

        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1

        return res