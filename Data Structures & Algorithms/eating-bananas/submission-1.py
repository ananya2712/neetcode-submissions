class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = sum(piles)
        speed = s // h
        while speed:
            totalHours = 0
            for pile in piles:
                totalHours = totalHours + math.ceil(pile/speed)
            if totalHours <=h:
                return speed
            speed = speed + 1
