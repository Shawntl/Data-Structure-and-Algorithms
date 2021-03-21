#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        left_brackets = '({['
        right_brackets = ')}]'
        if s[0] in right_brackets or len(s) % 2 != 0:
            return False
        stack = []
        for bracket in s:
            if bracket in left_brackets:
                stack.append(bracket)
            elif bracket in right_brackets:
                if len(stack) == 0:
                    return False
                pair = stack[-1]
                if left_brackets.index(pair) == right_brackets.index(bracket):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        
# @lc code=end

