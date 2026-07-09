class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = []
        for i in range(len(nums)):
            cache.append(nums[i])
        
        for i in range(1,len(nums)):
            cache[i] = max(nums[i], nums[i] + cache[i - 1])

        return max(cache)