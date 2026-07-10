class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] = count[num] + 1
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort()

        i = 0 
        res = []
        while i < k:
            tmp = arr.pop(-1)
            res.append(tmp[1])
            i+=1
        return res




