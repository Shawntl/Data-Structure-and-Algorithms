#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        strMat = [[0]*m for _ in range(n)]
        if text1[0] == text2[0]:
            strMat[0][0] = 1
        else:
            strMat[0][0] = 0
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    strMat[i][j] = max(strMat[i][j-1], 
                                       int(text1[i] == text2[j]))
                elif i != 0 and j == 0:
                    strMat[i][j] = max(strMat[i-1][j], 
                                       int(text1[i] == text2[j]))
                else:
                    if text1[i] == text2[j]:
                        strMat[i][j] = strMat[i-1][j-1] + 1
                    else:
                        strMat[i][j] = max(strMat[i-1][j], strMat[i][j-1]) 

        return strMat[i][j]     
# @lc code=end

