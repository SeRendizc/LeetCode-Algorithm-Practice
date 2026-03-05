#
# @lc app=leetcode.cn id=124 lang=python3
# @lcpr version=30204
#
# [124] 二叉树中的最大路径和
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = -1001
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.maxPath = max(self.maxPath, left + right + root.val)
            return max(0, max(left, right) + root.val)
        print(dfs(root))
        return self.maxPath

        # def findMax(curr: Optional[TreeNode]) -> int:
        #     if curr.left is None and curr.right is None:  # 抵达叶子
        #         self.maxPath = max(self.maxPath, curr.val)
        #         return curr.val
        #     if curr.left is None:
        #         currMax = max(curr.val, findMax(curr.right) + curr.val)
        #         self.maxPath = max(self.maxPath, currMax, curr.val)
        #         return currMax
        #     elif curr.right is None:
        #         currMax = max(curr.val, findMax(curr.left) + curr.val)
        #         self.maxPath = max(self.maxPath, currMax, curr.val)
        #         return currMax
        #     else:
        #         leftMax = findMax(curr.left)
        #         rightMax = findMax(curr.right)
        #         currMax = max(curr.val, leftMax + curr.val, rightMax + curr.val)
        #         self.maxPath = max(self.maxPath, currMax, leftMax + curr.val + rightMax, curr.val)
        #         return currMax
        # rootMax = findMax(root)
        # return max(rootMax, self.maxPath)
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-10,9,20,null,null,15,7]\n
# @lcpr case=end

#

