# @lcpr-before-debug-begin
from python3problem53 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [nums[0]] + [-100000] * n
        curr = 1
        maxn = nums[0]
        while curr < n:
            dp[curr] = max(nums[curr], dp[curr - 1] + nums[curr])
            maxn = max(maxn, dp[curr])
            curr += 1
        return maxn
# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

