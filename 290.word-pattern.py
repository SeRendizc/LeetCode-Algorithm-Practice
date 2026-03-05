# @lcpr-before-debug-begin
from python3problem290 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=290 lang=python3
# @lcpr version=30204
#
# [290] 单词规律
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        idx_n = {}
        idx_m = {}
        n = len(s_list)
        m = len(pattern)
        ans_n = []
        ans_m = []

        for i in range(n):
            if s_list[i] not in idx_n:
                idx_n[s_list[i]] = len(idx_n)
        for j in range(m):
            if pattern[j] not in idx_m:
                idx_m[pattern[j]] = len(idx_m)
        
        for i in range(n):
            ans_n.append(idx_n[s_list[i]])
        for j in range(m):
            ans_m.append(idx_m[pattern[j]])
        
        return ans_n == ans_m

# @lc code=end



#
# @lcpr case=start
# "abba"\n"dog cat cat dog"\n
# @lcpr case=end

# @lcpr case=start
# "abba"\n"dog cat cat fish"\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n"dog cat cat dog"\n
# @lcpr case=end

#

