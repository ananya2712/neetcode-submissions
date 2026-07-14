class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        start = 0
        res = 0

        for end in range(0,len(s)):
            while s[end] in visited:
                visited.remove(s[start])
                start = start + 1
            visited.add(s[end])
            res = max(res, end - start + 1)
            
        return res