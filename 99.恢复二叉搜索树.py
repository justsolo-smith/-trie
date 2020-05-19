#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root,low=float('-inf'),unper=float('inf')):
            if not root:
                return None
            val = root.val
            if root.right and val>=unper:
                root,root.right = root.right,root
            if root.left and val <=low:
                root,root.left = root.left,root
            helper(root.left,low,val)
            helper(root.right,val,unper)
            return root
        return helper(root)
        
# @lc code=end

