#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return self.a(nums)

    def a(self, nums: List[int]) -> int:
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]


# @lc code=end
