#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        h, res = [], []
        for key, val in dic.items():
            heapq.heappush(h, (-val, key))
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
        return res
        
# @lc code=end

