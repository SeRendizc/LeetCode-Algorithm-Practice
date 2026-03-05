#
# @lc app=leetcode.cn id=120 lang=python3
# @lcpr version=30204
#
# [120] 三角形最小路径和
#
from typing import List


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]
# @lc code=end



#
# @lcpr case=start
# [[2],[3,4],[6,5,7],[4,1,8,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[-10]]\n
# @lcpr case=end

#

