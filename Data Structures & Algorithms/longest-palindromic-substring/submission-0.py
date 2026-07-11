class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIndex = 0
        resLen = 0

        for i in range(0,len(s)):
            # odd lengths
            l,r = i,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIndex = l
                    resLen = r - l + 1
                l = l - 1
                r = r + 1
            
            # even lengths
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIndex = l
                    resLen = r - l + 1
                l = l - 1
                r = r + 1

        return s[resIndex:resIndex + resLen]