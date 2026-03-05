# @lcpr-before-debug-begin
from python3problem3 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        cur_len = 0
        max_len = 0
        win = set()
        for i in range(len(s)):
            cur_len += 1
            while s[i] in win:
                win.remove(s[left])
                left += 1
                cur_len -= 1
            max_len = max(max_len, cur_len)
            win.add(s[i])
        return max_len
        
        # TOO LONG TIME
        # i = 0
        # ans = 0
        # flag = 0
        # curr = []
        # while i < len(s):
        #     if s[i] not in curr:
        #         curr.append(s[i])
        #         flag = 1
        #         i += 1
        #     else:
        #         ans = max(ans, len(curr))
        #         i -= len(curr) - 1
        #         curr = []
        # return max(flag, ans, len(curr))
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

