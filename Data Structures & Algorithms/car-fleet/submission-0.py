class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mapped = []
        stk = []
        for i in range(0,len(position)):
            mapped.append((position[i],speed[i]))
        
        # sort based on position in desc order
        mapped.sort(reverse = True)

        # calculate time taken to reach target
        # formula => target - posiiton / speed

        for pos,speed in mapped:
            time = (target - pos) / speed
            stk.append(time)
            if len(stk) >= 2 and stk[-1] <= stk[-2]: # check if topmost time more than prev, then new fleet
                stk.pop() 
        return len(stk)