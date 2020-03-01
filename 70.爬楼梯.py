#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [0, 1, 2]
        for i in range(3, n + 1):
            nums.append(nums[i - 1] + nums[i - 2])
        return nums[n]


# @lc code=end
