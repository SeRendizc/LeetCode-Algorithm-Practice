# @lcpr-before-debug-begin
from python3problem274 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=274 lang=python3
# @lcpr version=30204
#
# [274] H 指数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 1: return min(citations[0], 1)
        citations.sort(reverse = True)
        h = 1
        while h <= n:
            for i in range(h):
                if citations[i] < h:
                    return h - 1
            h += 1
        return h - 1
# @lc code=end



#
# @lcpr case=start
# [3,0,6,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1]\n
# @lcpr case=end

#

