class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            if i == len(nums) -1:
                return 0
            if nums[i] == 0:
                return 9999999

            res = 9999999
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                res = min(res, 1 + dfs(j))
            dp[i] = res
            return res

        return dfs(0)