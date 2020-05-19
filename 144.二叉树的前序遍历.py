#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        white,black = 0,1
        res = []
        stack = [(white,root)]
        while stack:
            color,node = stack.pop()
            if node is None:continue
            if color == white:
                stack.append((white,node.right))
                stack.append((white,node.left))
                stack.append((black,node))
            else:
                res.append(node.val)
        return res

# @lc code=end

