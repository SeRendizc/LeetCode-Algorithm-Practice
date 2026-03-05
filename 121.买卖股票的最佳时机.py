#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 2147483647
        profit = 0
        for i in range(0, len(prices)):
            min_price = min(min_price, prices[i])
            if prices[i] > min_price:
                profit = max(profit, prices[i] - min_price)
        return profit
# @lc code=end

