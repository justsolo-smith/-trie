#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.res = True
        self.helper(root)
        return self.res
    def helper(self,root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if abs(left-right) >1:
            self.res = False
            return False
        return max(left,right)+1
        
# @lc code=end

