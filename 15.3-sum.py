# @lcpr-before-debug-begin
from python3problem15 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30204
#
# [15] 三数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        
        
        # nums.sort()
        # n = len(nums)
        # ans = []

        # for i in range(n - 2):
        #     # 最小的三个数之和已大于 0，后面不可能有解
        #     if nums[i] > 0:
        #         break
        #     # 跳过重复的 i
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue

        #     l, r = i + 1, n - 1
        #     while l < r:
        #         s = nums[i] + nums[l] + nums[r]
        #         if s == 0:
        #             ans.append([nums[i], nums[l], nums[r]])
        #             # 跳过重复的 l 和 r
        #             while l < r and nums[l] == nums[l + 1]:
        #                 l += 1
        #             while l < r and nums[r] == nums[r - 1]:
        #                 r -= 1
        #             l += 1
        #             r -= 1
        #         elif s < 0:
        #             l += 1
        #         else:
        #             r -= 1

        # return ans


        
        # n = len(nums)
        # ans = []
        
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         cal = nums[i] + nums[j]
        #         for k in range(j + 1, n):
        #             if cal + nums[k] == 0 and [nums[i],nums[j],nums[k]] not in ans and [nums[i],nums[k],nums[j]] not in ans and [nums[k],nums[i],nums[j]] not in ans and [nums[k],nums[j],nums[i]] not in ans and [nums[j],nums[i],nums[k]] not in ans and [nums[j],nums[k],nums[i]] not in ans:
        #                 ans.append([nums[i],nums[j],nums[k]])
        #             if i == n - 3 and j == n - 2 and k == n - 1:
        #                 return ans
# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

