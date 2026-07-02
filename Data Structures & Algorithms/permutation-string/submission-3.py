from itertools import permutations
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # BRUTE FORCE
        # perms = [''.join(p) for p in permutations(s1)]

        # for perm in perms:
        #     if perm in s2:
        #         return True
        # return False

        # know window size is len(s1)
        n = len(s1)
        s1_set = collections.Counter(s1)
        s2_window_set = collections.Counter()

        for i in range(0, len(s2) - n + 1):
            s = s2[i:i+n]
            s2_window_set = collections.Counter(s)

            if s2_window_set == s1_set:
                return True
            else:
                s2_window_set = set()
        return False
            
            

        

        
