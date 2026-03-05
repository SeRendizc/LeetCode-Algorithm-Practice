#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30204
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right)
        
        # if root.left == None and root.right == None:
        #     return True
        # if root.left == None or root.right == None:
        #     return False
        # def find(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        #     if left.val != right.val:
        #         return False
        #     if left.left == None and left.right == None and right.left == None and right.right == None:
        #         return True
        #     if left.left == None and right.right == None and left.right and right.left:
        #         return find(left.right, right.left)
        #     elif left.right == None and right.left == None and left.left and right.right:
        #         return find(left.left, right.right)
        #     elif left.left == None or left.right == None or right.left == None or right.right == None:
        #         return False
        #     return find(left.left, right.right) and find(left.right, right.left)
        # # print(root)
        # return find(root.left, root.right)
# @lc code=end



#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#

