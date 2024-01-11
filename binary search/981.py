import collections

class TimeMap:

    def __init__(self):
        self.values = collections.defaultdict(list)
        self.timestamps = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append(value)
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.values:
            return ""
        
        if timestamp >= self.timestamps[key][-1]:
            return self.values[key][-1]

        timestamps = self.timestamps[key]

        left = 0
        right = len(timestamps)-1

        ans = -1
        while left <= right:
            mid = (left + right) // 2

            if timestamps[mid] <= timestamp:
                ans = mid
                left = mid+1
            else:
                right = mid-1
        
        return "" if ans < 0 else self.values[key][ans]
        
