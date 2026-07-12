class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])

        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        res = []

        for pair in intervals:
            # completely overlapping
            start = pair[0]
            end = pair[1]

            if curr_start <= start and curr_end >= end:
                continue

            # partially overlapping
            elif curr_start <= start and curr_end >= start:
                curr_end = end

            # new interval
            else:
                res.append([curr_start,curr_end])
                curr_start = start
                curr_end = end
        res.append([curr_start,curr_end])
        intervals = res
        return intervals