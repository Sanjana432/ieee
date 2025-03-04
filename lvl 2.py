import bisect

class IntervalMerger:
    def __init__(self):
        self.intervals = []

    def addInterval(self, start: int, end: int):
        new_interval = [start, end]
        
        # Use binary search to find the correct insertion point in sorted intervals
        idx = bisect.bisect_right(self.intervals, new_interval)

        # Merge with the previous overlapping interval
        if idx > 0 and self.intervals[idx - 1][1] >= start:
            start = self.intervals[idx - 1][0]
            end = max(self.intervals[idx - 1][1], end)
            self.intervals.pop(idx - 1)

        # Merge with the next overlapping intervals
        while idx < len(self.intervals) and self.intervals[idx][0] <= end:
            end = max(end, self.intervals[idx][1])
            self.intervals.pop(idx)

        self.intervals.insert(idx, [start, end])

    def getIntervals(self):
        return self.intervals
