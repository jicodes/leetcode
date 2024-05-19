from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_count, s_count = {}, {}
        for i in range(len(p)):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        res = [0] if s_count == p_count else []
        left = 0
        for r in range(len(p), len(s)):
            s_count[s[r]] = s_count.get(s[r], 0) + 1
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                s_count.pop(s[left])
            left += 1
            if s_count == p_count:
                res.append(left)
        return res
