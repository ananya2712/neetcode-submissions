class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n

        def dfs(i):
            if i > n:
                return False
            if i == n:
                return True
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = dfs(i+1) + dfs(i+2)
            return dp[i]
        
        return dfs(0)