# @lcpr-before-debug-begin
from python3problem5 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30204
#
# [5] 最长回文子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s
        maxl = 1
        flag = 0
        dp = [[False for _ in range(n)] for _ in range(n)]

        for _ in range(n): dp[_][_] = True

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if length <= 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                if dp[i][j] and length > maxl:
                    maxl = length
                    flag = i
        
        return s[flag : flag + maxl]



# @lc code=end



#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

