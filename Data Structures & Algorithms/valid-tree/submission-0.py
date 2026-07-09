class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # adjacency graph and then dfs
        graph = {i : [] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(i, parent):
            if visited[i]:
                return False
            visited[i] = True
            
            for v in graph[i]:
                if v == parent:
                    continue
                if not dfs(v, i):
                    return False
            return True
        
        if not dfs(0, -1): # only need to run for one node and check if all are visited
            return False
        return all(visited)