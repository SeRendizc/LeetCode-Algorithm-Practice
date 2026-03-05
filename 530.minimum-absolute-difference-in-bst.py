# @lcpr-before-debug-begin
from python3problem530 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=530 lang=python3
# @lcpr version=30204
#
# [530] 二叉搜索树的最小绝对差
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDiff = 1 << 31
        def findMin(root):
            if not root:
                return None
            left = findMin(root.left)
            right = findMin(root.right)
            if left:
                leftmin = left[0]
                leftmax = left[1]
            else:
                leftmin = root.val
                leftmax = -3000000
            if right:
                rightmin = right[0]
                rightmax = right[1]
            else:
                rightmax = root.val
                rightmin = 3000000
            self.minDiff = min(self.minDiff, root.val - leftmax, rightmin - root.val)
            ans =  []
            ans.append(leftmin)
            ans.append(rightmax)
            return ans
        print(findMin(root))
        return self.minDiff

# @lc code=end



#
# @lcpr case=start
# [4,2,6,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,48,null,null,12,49]\n
# @lcpr case=end

#

