#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30204
#
# [198] 打家劫舍
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxrob = 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0] + nums[2], nums[1])
        dp = [nums[0]] + [nums[1]] + [nums[0] + nums[2]] + [-1] * n
        for i in range(3):
            maxrob = max(dp[i], maxrob)
        for i in range(3, n):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
            maxrob = max(dp[i], maxrob)
        return maxrob

# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#

