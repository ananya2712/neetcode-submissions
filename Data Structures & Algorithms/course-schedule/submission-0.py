class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency list and then run dfs and check all nodes visited
        visited = [False] * numCourses
        components = 0
        graph = {i: [] for i in range(numCourses)}
        for u,v in prerequisites:
            graph[u].append(v)
        
        def dfs(i):
            if visited[i] == True:
                return False # cycle found
            if graph[i] == []:
                return True

            visited[i] = True
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = False
            graph[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        
