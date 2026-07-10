class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minProd, maxProd = 1,1

        for i in range(0,len(nums)):
            temp = maxProd * nums[i]
            maxProd = max(nums[i], nums[i]*maxProd, nums[i]*minProd)
            minProd = min(nums[i], temp, nums[i]*minProd)
            res = max(maxProd,res)

        return res

      
            
