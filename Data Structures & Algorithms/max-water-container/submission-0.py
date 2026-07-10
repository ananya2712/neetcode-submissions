class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        cap = 0

        while l < r:
            temp = (r-l) * min(heights[l],heights[r])
            cap = max(temp,cap)
            
            if heights[l] > heights[r]:
                r = r - 1
            else:
                l = l + 1
        return cap