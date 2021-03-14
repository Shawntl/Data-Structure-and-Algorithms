#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for gram in strs:
            key = ''.join(sorted(gram))
            if key in anagram_dict.keys():
                anagram_dict[key].append(gram)
            else:
                anagram_dict[key] = [gram]
        return [group for group in anagram_dict.values()]

        
# @lc code=end

