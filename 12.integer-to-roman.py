#
# @lc app=leetcode.cn id=12 lang=python3
# @lcpr version=30204
#
# [12] 整数转罗马数字
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [0] * 3
        ans = []
        tzds = num // 1000
        nums[0] = num // 100 % 10
        nums[1] = num // 10 % 10
        nums[2] = num % 10
        num123 = ['C', 'X', 'I']
        num4 = ['CD', 'XL', 'IV']
        num5 = ['D', 'L', 'V']
        num9 = ['CM', 'XC', 'IX']

        while tzds:
            ans.append('M')
            tzds -= 1
        
        for i in range(3):
            if nums[i] == 9: ans.append(num9[i])
            elif nums[i] == 4: ans.append(num4[i])
            else:
                if nums[i] >= 5:
                    ans.append(num5[i])
                    nums[i] -= 5
                while nums[i]:
                    ans.append(num123[i])
                    nums[i] -= 1

        return ''.join(ans)

# @lc code=end



#
# @lcpr case=start
# 3749\n
# @lcpr case=end

# @lcpr case=start
# 58\n
# @lcpr case=end

# @lcpr case=start
# 1994\n
# @lcpr case=end

#

