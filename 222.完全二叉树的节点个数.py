#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.countNodes(root.left)
        self.res.append(root.val)
        self.countNodes(root.right)
        return len(self.res)
# @lc code=end

