#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 2: return True

        def isPalindrome(l):
            start, end = 0, len(l) - 1
            while start < end:
                if l[start] == l[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left:right]) or isPalindrome(s[left+1:right+1])
        return True
        
# @lc code=end

