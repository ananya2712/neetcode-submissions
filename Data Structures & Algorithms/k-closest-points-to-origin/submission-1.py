import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # points.sort(key=lambda p: math.hypot(p[0], p[1]))
        # return points[:k] 

        res = []
        for x, y in points:
            dis = math.sqrt(x**2 + y**2)
            res.append([dis,x,y])
        
        heapq.heapify(res)
        final = []
        while k>0:
            dis,x,y = heapq.heappop(res)
            final.append([x,y])
            k = k - 1

        return final

