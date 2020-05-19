#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.stack = []
        while True:
            while root:
                self.stack.append(root)
                root = root.left
            root = self.stack.pop()
            k -=1
            if not k:
                return root.val
            root = root.right   
# @lc code=end

