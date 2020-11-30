#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#

# @lc code=start
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        max_length = 0
        max_idx = -1
        for i, string in enumerate(d):
            m, n, cur_length = 0, 0, 0
            while m < len(s) and n < len(string):
                if s[m] == string[n]:
                    cur_length += 1
                    m += 1
                    n += 1
                else:
                    m += 1
            if n < len(string):
                continue
            if cur_length > max_length:
                max_length = cur_length
                max_idx = i
            elif cur_length == max_length:
                if string < d[max_idx]:
                    max_idx = i
                else:
                    continue

        if max_idx == -1:
            return ''
        return d[max_idx]
# @lc code=end

