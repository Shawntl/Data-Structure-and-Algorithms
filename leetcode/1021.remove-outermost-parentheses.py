#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, stack = '', []
        for bracket in S:
            if bracket == '(':
                if stack: res += bracket
                stack.append(bracket)
            elif bracket == ')':
                stack.pop()
                if stack: res += bracket

        return res


        
# @lc code=end

