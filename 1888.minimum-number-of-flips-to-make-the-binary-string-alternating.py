#
# @lc app=leetcode.cn id=1888 lang=python3
# @lcpr version=30204
#
# [1888] 使二进制字符串字符交替的最少反转次数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        double_s = s + s
        diff1 = 0  # pattern1[i] = str(i % 2)
        diff2 = 0  # pattern2[i] = str(1 - i % 2)
        
        for i in range(n):
            if double_s[i] != str(i % 2):
                diff1 += 1
            if double_s[i] != str(1 - i % 2):
                diff2 += 1
        
        min_flips = min(diff1, diff2)
        
        for start in range(1, n):
            left = start - 1  # 离开字符
            right = start + n - 1  # 进入字符
            
            if double_s[left] != str(left % 2):
                diff1 -= 1
            if double_s[left] != str(1 - left % 2):
                diff2 -= 1
            
            if double_s[right] != str(right % 2):
                diff1 += 1
            if double_s[right] != str(1 - right % 2):
                diff2 += 1
            
            min_flips = min(min_flips, diff1, diff2)
        
        return min_flips
# @lc code=end



#
# @lcpr case=start
# "111000"\n
# @lcpr case=end

# @lcpr case=start
# "010"\n
# @lcpr case=end

# @lcpr case=start
# "1110"\n
# @lcpr case=end

#

