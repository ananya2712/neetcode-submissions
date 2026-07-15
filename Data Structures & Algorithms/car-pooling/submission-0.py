class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])

        for i in range(len(trips)):
            curr = trips[i][0]

            for j in range(i): # how many passengers already there
                if trips[j][2] > trips[i][1]:
                    curr +=trips[j][0]
            if curr > capacity:
                return False
        return True