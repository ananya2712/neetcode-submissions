class TimeMap:

    def __init__(self):
        self.timestamps = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps:
            self.timestamps[key] = []
        self.timestamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""
            
        pairs = self.timestamps[key]
        lo, hi = 0, len(pairs) - 1
        res = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return res



        
