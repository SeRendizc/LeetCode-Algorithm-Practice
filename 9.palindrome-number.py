#
# @lc app=leetcode.cn id=9 lang=python3
# @lcpr version=30204
#
# [9] 回文数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0 or (x % 10 == 0 and x != 0):
        #     return False
        # reversed_half = 0
        # while x > reversed_half:         # 只翻转一半
        #     reversed_half = reversed_half * 10 + x % 10
        #     x //= 10
        # return x == reversed_half or x == reversed_half // 10
        
        if x < 0: return False
        s = f'{x}'
        return s == s[::-1]
        
        
        # if x < 0: return False
        # s = str(x)
        # n = len(s)
        # i = 0
        # isPal = True
        # while i < n - i - 1:
        #     if s[i] != s[n - i - 1]: isPal = False
        #     i += 1
        # return isPal
# @lc code=end



#
# @lcpr case=start
# 121\n
# @lcpr case=end

# @lcpr case=start
# -121\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#

