#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30204
#
# [238] 除了自身以外数组的乘积
#
from typing import List

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        left_product = 1
        right_product = 1

        for i in range(n):
            ans[i] *= left_product
            left_product *= nums[i]
        
        for i in range(n-1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
        
        return ans

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

