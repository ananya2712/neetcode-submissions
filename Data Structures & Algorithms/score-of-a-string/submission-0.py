class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        i = 0
        while i < len(s) - 1:
            sum = sum + abs(ord(s[i+1]) - ord(s[i]))
            i = i + 1
        return sum