# @lcpr-before-debug-begin
from python3problem104 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=104 lang=python3
# @lcpr version=30204
#
# [104] 二叉树的最大深度
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        self.maxlayer = 0
        def searchmax(root: Optional[TreeNode], layer: int) -> int:
            if root.left == None and root.right == None:
                return layer
            if root.left:
                maxl = searchmax(root.left, layer + 1)
                self.maxlayer = max(self.maxlayer, maxl)
            if root.right:
                maxl = searchmax(root.right, layer + 1)
                self.maxlayer = max(self.maxlayer, maxl)
            return layer
        maxl = searchmax(root, 1)
        self.maxlayer = max(self.maxlayer, maxl)
        return self.maxlayer
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#

