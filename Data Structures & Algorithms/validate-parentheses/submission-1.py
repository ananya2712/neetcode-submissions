class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for char in s:
            if char == '[' or char == '(' or char == '{':
                stk.append(char)
            elif stk and char == ']' and stk[-1] == '[':
                stk.pop()
            elif stk and char == '}' and stk[-1] == '{':
                stk.pop()
            elif stk and char == ')' and stk[-1] == '(':
                stk.pop()
            else:
                return False
        if stk == []:
            return True
        return False