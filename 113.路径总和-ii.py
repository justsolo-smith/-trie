# @before-stub-for-debug-begin
from python3problem113 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
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
        self.res = 0
        self.a = []
        self.b = []
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        val = root.val
        self.a.append(val)
        self.res +=val
        if sum==self.res and not root.left and not root.right:
            self.b.append(self.a[:])
        else:
            self.pathSum(root.left,sum)
            self.pathSum(root.right,sum)
        self.res -= self.a[-1]
        self.a.pop()
        return self.b


# @lc code=end

