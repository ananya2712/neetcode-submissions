import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: math.hypot(p[0], p[1]))
        return points[:k] 

