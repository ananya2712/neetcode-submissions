class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(0,len(nums)):
            hashmap[nums[i]] = i
        
        for i,num in enumerate(nums):
            if target - num in hashmap and hashmap[target - num] !=i:
                return [i,hashmap[target - num]]

        return []