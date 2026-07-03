class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        if list(s) == nums:
            return False
        else:
            return True