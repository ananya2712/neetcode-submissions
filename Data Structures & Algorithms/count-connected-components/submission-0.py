class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adjacency list 
        visited = [False] * n
        components = 0
        graph = {i: [] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(i):
            visited[i] = True
            for j in graph[i]:
                if not visited[j]:
                    dfs(j)
        
        for i in range(0,n):
            if not visited[i]:
                components +=1
                dfs(i)
        return components
            
            