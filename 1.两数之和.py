#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            temp = target - nums[i]
            try:
                index = map[temp]
                if i != index:
                    return [i, index]
            except:
                continue


# @lc code=end
