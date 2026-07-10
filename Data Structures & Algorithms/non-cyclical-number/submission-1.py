class Solution:
    def isHappy(self, n: int) -> bool:
        s = 0
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.computeNum(n)
            if n == 1:
                return True
            
        return False
        

    def computeNum(self,n):
        s = 0
        while n != 0 :
            last_digit = n % 10
            n = n // 10
            s = s + math.pow(last_digit,2)
            
        return s

