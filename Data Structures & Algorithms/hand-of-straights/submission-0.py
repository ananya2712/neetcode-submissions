class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize !=0:
            return False

        hashmap = Counter(hand)
        hand.sort()

        for num in hand:
            if hashmap[num]:
                for i in range(num, num + groupSize):
                    if not hashmap[i]:
                        return False
                    hashmap[i] = hashmap[i] - 1

        return True
        









        
        