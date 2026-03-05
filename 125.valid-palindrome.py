#
# @lc app=leetcode.cn id=125 lang=python3
# @lcpr version=30204
#
# [125] 验证回文串
#

import re
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s_edited = re.sub(r'[^a-z0-9]', '', s_lower)
        n = len(s_edited)
        left = 0
        right = n - 1
        # print(s_lower)
        # print(s_edited)
        while left < right:
            if s_edited[left] != s_edited[right]:
                return False
            left += 1
            right -= 1
        
        return True
# @lc code=end



#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#

