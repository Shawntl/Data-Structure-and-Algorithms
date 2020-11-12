#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    #     sort_lst = sorted(nums)
    #     miss_num = 1
    #     if sort_lst[-1] != len(sort_lst):
    #         miss_num = len(sort_lst)
    #     for i in range(1, len(sort_lst)):
    #         if (sort_lst[i] - sort_lst[i-1]) == 1:
    #             continue
    #         if sort_lst[i] == sort_lst[i-1]:
    #             repeti_num = sort_lst[i]
    #         if sort_lst[i] - sort_lst[i-1] == 2:
    #             miss_num = sort_lst[i] - 1
    #     return [repeti_num, miss_num]

    # solution two(map)
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    #     from collections import Counter
    #     res_dict = Counter(nums)
    #     for i in range(1, len(nums) + 1):
    #         if i not in res_dict:
    #             miss_num = i
    #         if res_dict[i] == 2:
    #             repeti_num = i
    #     return [repeti_num, miss_num]

    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = ((1+n)*n) / 2
        lack = total - sum(set(nums))
        repeti = sum(nums) + lack - total

        return [int(repeti), int(lack)1]
# @lc code=end

