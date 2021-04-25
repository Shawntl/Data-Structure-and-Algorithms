#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        res = []
        p_dict = collections.Counter(p)
        sub_s_dict = collections.Counter(s[0:m])
        if p_dict == sub_s_dict:
            res.append(0)
        for i in range(1, n-m+1):
            if sub_s_dict[s[i-1]] > 1:
                sub_s_dict[s[i-1]] -= 1
            else:
                del sub_s_dict[s[i-1]]
            if s[i+m-1] in sub_s_dict.keys():
                sub_s_dict[s[i+m-1]] += 1
            else:
                sub_s_dict[s[i+m-1]] = 1
            if sub_s_dict == p_dict:
                res.append(i)

        return res
# @lc code=end

