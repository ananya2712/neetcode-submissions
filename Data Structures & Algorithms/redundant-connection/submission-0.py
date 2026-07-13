class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n + 1)]

        def dfs(i, par):
            if visited[i] == True:
                return True # cycle found

            visited[i] = True
            for neighbor in graph[i]:
                if neighbor == par:
                    continue
                if dfs(neighbor, i):
                    return True
            return False

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            visited = [False] * (n + 1)

            if dfs(u, -1):
                return [u,v]
        return []

