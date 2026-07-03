from itertools import permutations

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
        s1_set = set(s1)
        s2_window_set = set()

        for i in range(0, len(s2) - n + 1):
            start = i 
            end = i + n
            for j in range(start, end):
                s2_window_set.add(s2[j])

            if s2_window_set == s1_set:
                return True
            else:
                s2_window_set = set()
        return False
            
            

        

        
