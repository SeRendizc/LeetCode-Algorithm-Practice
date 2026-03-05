# @lcpr-before-debug-begin
from python3problem228 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=228 lang=python3
# @lcpr version=30204
#
# [228] 汇总区间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        ans = []

        left = 0
        while left < n:
            right = left
            while right + 1 < n and nums[right] + 1 == nums[right + 1]:
                right += 1

            if right == left:
                ans.append(f"{nums[left]}")
            else:
                ans.append(f"{nums[left]}->{nums[right]}")


            left = right + 1

        return ans
# @lc code=end



#
# @lcpr case=start
# [0,1,2,4,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,2,3,4,6,8,9]\n
# @lcpr case=end

#

