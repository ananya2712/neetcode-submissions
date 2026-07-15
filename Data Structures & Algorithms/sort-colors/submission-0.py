class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] +=1
        
        idx = 0
        for i in range(0,3):
            while hashmap[i] > 0:
                nums[idx] = i
                hashmap[i] -=1
                idx = idx + 1