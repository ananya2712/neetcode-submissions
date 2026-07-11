class Solution:
    def checkValidString(self, s: str) -> bool:
        lefts = []   # indices of unmatched '('
        stars = []   # indices of unused '*'
        for i, ch in enumerate(s):
            if ch == '(':
                lefts.append(i)
            elif ch == '*':
                stars.append(i)
            else:
                if lefts:
                    lefts.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        while lefts and stars:
            if lefts.pop() > stars.pop():
                return False
        return not lefts