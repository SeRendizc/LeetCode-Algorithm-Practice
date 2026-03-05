# @lcpr-before-debug-begin
from python3problem200 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30204
#
# [200] 岛屿数量
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        def delIsland(i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return False
            if grid[i][j] == '0':
                return False
            grid[i][j] = '0'
            a = delIsland(i - 1, j)
            a = delIsland(i + 1, j)
            a = delIsland(i, j - 1)
            a = delIsland(i, j + 1)
            return True
        
        for i in range(m):
            for j in range(n):
                ans += delIsland(i, j)
        
        return ans
# @lc code=end



#
# @lcpr case=start
# [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]\n
# @lcpr case=end

# @lcpr case=start
# [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]\n
# @lcpr case=end

#

