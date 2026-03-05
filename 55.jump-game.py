# @lcpr-before-debug-begin
from python3problem55 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30204
#
# [55] 跳跃游戏
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, step in enumerate(nums):
            if i > farthest: return False
            farthest = max(farthest, i + step)
            if farthest >= len(nums) - 1: return True
        return True


















        # farthest = 0
        # for i, step in enumerate(nums):
        #     if i > farthest:
        #         return False
        #     farthest = max(farthest, i + step)
        #     if farthest >= len(nums) - 1:
        #         return True
        # return True
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#

