#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30204
#
# [11] 盛最多水的容器
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_size = 0

        while left < right:
            # cur_size = (right - left) * min(height[left], height[right])
            max_size = max(max_size, (right - left) * min(height[left], height[right]))

            if height[left] > height[right]: right -= 1  # 左高挪右
            else: left += 1
        
        return max_size

# @lc code=end



#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#

