#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_dic = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'}
        res = []
        n = len(digits)
        if n == 0:
            return []
        def backtrack(dig_idx, s):
            if dig_idx == n:
                res.append(s)
                return
            key = digits[dig_idx]
            for j in range(len(dig_dic[key])):
                backtrack(dig_idx+1, s+dig_dic[key][j])
        backtrack(0, '')
        return res
        
# @lc code=end

