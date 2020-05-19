# @before-stub-for-debug-begin
from python3problem129 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
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
        self.temp = 0
        self.res = []
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.temp = self.temp*10 + root.val
        self.sumNumbers(root.left)
        self.sumNumbers(root.right)
        if not root.left and not root.right:
            self.res.append(self.temp)
        self.temp = (self.temp - root.val)//10
        return sum(self.res)

# @lc code=end

