class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            x1 = stones.pop()
            x2 = stones.pop()

            if x1- x2 > 0:
                stones.append(x1-x2)
        
        if stones: 
            return stones[0]
        else:
            return 0