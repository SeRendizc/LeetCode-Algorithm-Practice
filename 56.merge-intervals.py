# @lcpr-before-debug-begin
from python3problem56 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30204
#
# [56] 合并区间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        if n == 1: return intervals
        ans = []
        left = 0
        right = 1
        while left < n:
            rightval = intervals[left][1]
            while right < n and rightval >= intervals[right][0]:
                rightval = max(rightval, intervals[right][1])
                right += 1
            ans.append([intervals[left][0], rightval])
            left = right
            right += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,7],[1,4]]\n
# @lcpr case=end

#

