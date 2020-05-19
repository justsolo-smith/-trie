# @before-stub-for-debug-begin
from python3problem98 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root,left=float('-inf'),right=float('inf')):
            if not root:
                return True
            if root.val<=left or root.val >=right:
                return False
            if not helper(root.left,left,root.val):
                return False
            if not helper(root.right,root.val,right):
                return False  
            return True
        return helper(root)
        
# @lc code=end

