class TimeMap:
    def __init__(self):
        self.data = {}  # key: list of tuples(value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        value_stamp_pairs = self.data[key]
        left, right = 0, len(value_stamp_pairs) - 1
        while left <= right:
            mid = (left + right) // 2
            if value_stamp_pairs[mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        # We continue this process until the search range is narrowed down to a single index `right`.
        # Now, when we exit the binary search loop, the variable `right` holds the index of the largest timestamp less than or equal to the given timestamp.
        if right >= 0:
            return value_stamp_pairs[right][0]
        return ""
