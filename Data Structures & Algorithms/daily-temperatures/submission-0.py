class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i,t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                stTemp, stIndex = stk.pop()
                res[stIndex] = i - stIndex
            stk.append((t,i))
        return res