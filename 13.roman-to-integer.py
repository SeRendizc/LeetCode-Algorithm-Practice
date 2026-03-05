#
# @lc app=leetcode.cn id=13 lang=python3
# @lcpr version=30204
#
# [13] 罗马数字转整数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
        
        for i in range(len(s)):
            if i < len(s) - 1 and val[s[i]] < val[s[i + 1]]:  # 4 or 9
                ans -= val[s[i]]
            else:
                ans += val[s[i]]
        
        return ans

# @lc code=end



#
# @lcpr case=start
# "III"\n
# @lcpr case=end

# @lcpr case=start
# "IV"\n
# @lcpr case=end

# @lcpr case=start
# "IX"\n
# @lcpr case=end

# @lcpr case=start
# "LVIII"\n
# @lcpr case=end

# @lcpr case=start
# "MCMXCIV"\n
# @lcpr case=end

#

