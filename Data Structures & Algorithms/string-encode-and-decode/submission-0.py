class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for s in strs:
            l = len(s)
            final = final + str(l) + '!' + s
        return final

    def decode(self, s: str) -> List[str]:
        res = [] 
        i = 0
        l = len(s)
        while i < l:
            j = i
            while s[j] !='!':
                j=j+1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
