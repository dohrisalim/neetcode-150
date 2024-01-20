class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ct, pt = 0, float("-inf")
        for p0, p1 in intervals:
            if p0 < pt:
                ct += 1
                pt = min(p1, pt)
            else:
                pt = p1
        
        return ct