# @lcpr-before-debug-begin
from python3problem205 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=205 lang=python3
# @lcpr version=30204
#
# [205] 同构字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        s_idx = {}
        t_idx = {}
        s_hash = []
        t_hash = []
        for i in range(n):
            if s[i] not in s_idx:
                s_idx[s[i]] = len(s_idx)
            if t[i] not in t_idx:
                t_idx[t[i]] = len(t_idx)
        for i in range(n):
            s_hash.append(s_idx[s[i]])
            t_hash.append(t_idx[t[i]])
        return s_hash == t_hash
                
# @lc code=end



#
# @lcpr case=start
# "egg"\n"add"\n
# @lcpr case=end

# @lcpr case=start
# "f11"\n"b23"\n
# @lcpr case=end

# @lcpr case=start
# "paper"\n"title"\n
# @lcpr case=end

#

