# @before-stub-for-debug-begin
from python3problem235 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left,p,q)
        # elif p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right,p,q)
        # else:
        #     return root
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root
           
# @lc code=end

