from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # Initialize the adjacency list
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Initialize the count of connections (degree) for each node and the initial leaves
        connection_count = {}
        leaves = deque()
        for node, neighbors in adj_list.items():
            connection_count[node] = len(neighbors)
            if len(neighbors) == 1:
                leaves.append(node)

        # Trim the leaves until 2 or fewer nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in adj_list[leaf]:
                    connection_count[neighbor] -= 1
                    if connection_count[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)
