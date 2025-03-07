import bisect

class IntervalMerger:
    def __init__(self):
        self.intervals = []  # Stores intervals sorted by start time

    def addInterval(self, start, end):
        new_interval = [start, end]
        # Insert the new interval in sorted order
        bisect.insort(self.intervals, new_interval)

        merged_intervals = []
        for interval in self.intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        self.intervals = merged_intervals

    def getIntervals(self):
        return self.intervals

# Usage Example
merger = IntervalMerger()
merger.addInterval(1, 5)
merger.addInterval(6, 8)
merger.addInterval(4, 7)
print(merger.getIntervals())  # Expected Output: [[1, 8]]

