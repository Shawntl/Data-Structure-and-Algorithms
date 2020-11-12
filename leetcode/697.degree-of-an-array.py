#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    # def findShortestSubArray(self, nums: List[int]) -> int:
    #     from collections import Counter
    #     degree_dic = Counter(nums)
    #     degree = max(degree_dic.values())
    #     gap = len(nums)
    #     reverse_nums = list(reversed(nums))
    #     for key in degree_dic:
    #         if degree_dic[key] == degree:
    #             first = nums.index(key)
    #             last = len(nums) - 1 - reverse_nums.index(key)
    #             gap = min(last - first + 1, gap)
    #     return gap 
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
# @lc code=end

