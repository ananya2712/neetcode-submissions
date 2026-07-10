class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        for num in nums:
            res.append(prod)
            prod = prod*num
            
        prod_suf = 1
        for i in range(len(nums)-1,-1, -1):
            res[i] = res[i]* prod_suf
            prod_suf = prod_suf * nums[i]
        
        return res
        
