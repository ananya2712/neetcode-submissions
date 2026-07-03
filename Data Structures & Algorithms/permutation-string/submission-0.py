from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perms = [''.join(p) for p in permutations(s1)]

        for perm in perms:
            if perm in s2:
                return True
        return False

        

        
