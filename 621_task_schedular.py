from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequencies of each task
        task_counts = Counter(tasks)

        # Extract the frequencies and sort them in descending order
        freq = list(task_counts.values())
        freq.sort(reverse=True)

        # Determine the maximum intervals needed for the most frequent task
        max_intervals_needed = freq[0] - 1
        idle = max_intervals_needed * n

        # Fill idle slots with remaining tasks
        for f in freq[1:]:
            idle -= min(max_intervals_needed, f)

        # Calculate and return the total time
        return len(tasks) + idle if idle > 0 else len(tasks)
