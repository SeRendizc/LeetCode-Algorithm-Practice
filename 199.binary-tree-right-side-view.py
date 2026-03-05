# @lcpr-before-debug-begin
from python3problem199 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=199 lang=python3
# @lcpr version=30204
#
# [199] 二叉树的右视图
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.right = [-150] * 100
        def findRight(root, layer):
            if not root:
                return
            if self.right[layer] == -150:
                self.right[layer] = root.val
            findRight(root.right, layer + 1)
            findRight(root.left, layer + 1)
        findRight(root, 0)
        ans = [_ for _ in self.right if _ != -150]
        print(root)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,null,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

