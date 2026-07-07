class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        
        def memoisation(i):
            if i >=len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cost[i] + min(memoisation(i+1), memoisation(i+2))
            return cache[i]

        return min(memoisation(0), memoisation(1))
