# Link: https://leetcode.com/problems/accounts-merge/
# union-find
from typing import List
import collections 

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = UnionFind()
        email_to_name = {}

        # Build union-find structure
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                union_find.union(email, account[1])

        # Group emails by their root parent
        groups = collections.defaultdict(list)
        for email in email_to_name:
            groups[union_find.find(email)].append(email)

        # Merge accounts
        result = []
        for root_parent, emails in groups.items():
            result.append([email_to_name[root_parent]] + sorted(emails))

        return result