class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        cache = [[False] * n for i in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j] and (j - i <=2 or cache[i+1][j-1]):
                    cache[i][j] = True
                    res+=1
        return res