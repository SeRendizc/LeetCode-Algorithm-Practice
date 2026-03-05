# @lcpr-before-debug-begin
from python3problem45 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30204
#
# [45] 跳跃游戏 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        dp = [0] + [20000] * (n - 1)
        for i, steps in enumerate(nums):
            for step in range(1, steps + 1):
                target = i + step
                if target > n - 1: break
                dp[target] = min(dp[target], dp[i] + 1)
                if target == n - 1: return dp[target]
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

