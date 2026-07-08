class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount+1)

        def dfs(i):
            if i>amount:
                return 0
            if i == 0:
                return 0
            if memo[i] != -1:
                return memo[i]

            res = 1e9
            for coin in coins:
                if i - coin >=0:
                    res = min(res, 1 + dfs(i-coin))
            memo[i] = res
            return res

        c = dfs(amount)
        if c >=1e9:
            return -1
        else:
            return c