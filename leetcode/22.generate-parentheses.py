#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left, right = 0, 0
        res = []

        def recurGenBracket(l, r, n, s):

            if l == n and r == n:
                res.append(s)
                return
            s1 = s + '('
            s2 = s + ')'
            if l < n:
                recurGenBracket(l+1, r, n, s1)
            if r < l:
                recurGenBracket(l, r+1, n, s2)
        recurGenBracket(left, right, n, '')
        return res
# @lc code=end

