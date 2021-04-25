#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # 若字符串长度为0或只有空格，返回0
        if len(s) == 0 or len(s.strip()) == 0: return 0
        # 除去前后的空格
        s = s.strip()

        # 判断数字前的符号
        sign = -1 if s[0] == '-' else 1
        # 如果第一位为符号，删除第一位
        if s[0] in '-+': s = s[1:]
        
        i, res = 0, 0
        while i < len(s) and s[i].isdigit():
            res = res*10 + (ord(s[i]) - ord('0'))
            i += 1
        return max(-2**31, min(res*sign, 2**31-1))

# @lc code=end

