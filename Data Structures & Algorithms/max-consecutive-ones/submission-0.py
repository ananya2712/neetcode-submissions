class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        curr = 0

        for i in range(0,len(nums)):
            if nums[i] == 1:
                curr = curr + 1
                m = max(curr,m)
            else:
                m = max(curr,m)
                curr = 0
        return m