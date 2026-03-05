# @lcpr-before-debug-begin
from python3problem54 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30204
#
# [54] 螺旋矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix[0])
        n = len(matrix)
        num = m * n
        up = 0
        down = n - 1
        left = 0
        right = m - 1

        while len(ans) < num:
            for i in range(left, right + 1): ans.append(matrix[up][i])
            if len(ans) == num: break
            for j in range(up + 1, down + 1): ans.append(matrix[j][right])
            if len(ans) == num: break
            for k in range(right - 1, left - 1, -1): ans.append(matrix[down][k])
            if len(ans) == num: break
            for l in range(down - 1, up, -1): ans.append(matrix[l][left])
            if len(ans) == num: break
            up += 1
            right -= 1
            down -= 1
            left += 1

        return ans
       
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

