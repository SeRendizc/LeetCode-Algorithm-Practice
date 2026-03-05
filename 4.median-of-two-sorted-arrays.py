# @lcpr-before-debug-begin
from python3problem4 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        k = 0
        m = len(nums1)
        n = len(nums2)
        total = m + n
        nums = [0] * total
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1
        if j < n:
            nums[k:] = nums2[j:]
        elif i < m:
            nums[k:] = nums1[i:]
        if total % 2:
            return float(nums[total // 2])
        else:
            return float((nums[total // 2 - 1] + nums[total // 2]) / 2)
# @lc code=end



#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#

