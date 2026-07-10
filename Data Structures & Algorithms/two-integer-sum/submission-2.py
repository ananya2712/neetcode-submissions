class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [] # create a copy 
        for i in range(0,len(nums)):
            arr.append([nums[i],i])

        arr.sort() 
        i, j = 0, len(arr) -1
        res = []
        while i < j:
            if arr[i][0] + arr[j][0] == target:
                res.append(arr[i][1])
                res.append(arr[j][1])
                break
            elif arr[i][0] + arr[j][0] < target:
                i = i + 1
            else:
                j = j - 1
        res.sort()
        return res

                