#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        if num == 0: return res
        cur_count = 0
        for i in range(1, num+1):
            if ((i-1) & 1) == 0:
                res.append(res[i-1] + 1)
            else:
                pre_1_cnt = 0
                pre_val = i-1
                while (pre_val & 1) == 1:
                    pre_val >>= 1
                    pre_1_cnt += 1
                res.append(res[i-1] - pre_1_cnt + 1)
        return res
        
# @lc code=end

