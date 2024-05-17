from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Compare each meeting with the next one
    for i in range(1, intervals.length()):
        # If the current meeting starts before the previous one ends, return False
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    # If no overlap is found, return True
    return True
