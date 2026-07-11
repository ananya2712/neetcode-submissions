class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])

        curr_start = intervals[0][0]
        curr_end = intervals[0][1]

        for i in range(1,len(intervals)):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]

            # fully lies in middle
            if curr_start <= start and curr_end >= end:
                continue

            # partially lies
            elif curr_start <= start and curr_end >= start:
                curr_end = end
            # start new
            else:
                res.append([curr_start,curr_end])
                curr_start = start
                curr_end = end
        
        res.append([curr_start,curr_end])
        return res