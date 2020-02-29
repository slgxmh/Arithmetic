#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        miniPrice = float("inf")
        maxProfit = 0
        for p in prices:
            if p < miniPrice:
                miniPrice = p
            tempProfit = p - miniPrice
            if tempProfit > maxProfit:
                maxProfit = tempProfit
        return maxProfit


# @lc code=end
