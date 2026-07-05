class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        res = max(piles)

        while start <=end:
            mid = start + (end - start) // 2
            total_hours = 0
            
            for p in piles:
                total_hours += math.ceil(p/mid)
            
            if total_hours <=h:
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        return res

