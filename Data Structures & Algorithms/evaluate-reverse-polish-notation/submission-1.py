class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token.isalnum():
                stk.append(int(token))
            elif token == '+':
                num1 = stk.pop(-1)
                num2 = stk.pop(-1)
                num = num1+ num2
                stk.append(num)
            elif token == '-':
                num1 = stk.pop(-1)
                num2 = stk.pop(-1)
                num = num1- num2
                stk.append(num)
            elif token == '*':
                num1 = stk.pop(-1)
                num2 = stk.pop(-1)
                num = num1 * num2
                stk.append(num)
            elif token == '/':
                num1 = stk.pop(-1)
                num2 = stk.pop(-1)
                num = num1 // num2
                stk.append(num)
            else:
                continue

        return stk.pop(-1)



