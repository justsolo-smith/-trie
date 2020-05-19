# @before-stub-for-debug-begin
from python3problem124 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_num = -20
        self.find(root)
        return self.max_num
    def find(self,node):
        if not node:
            return 0
        left = max(0,self.find(node.left))
        right = max(0,self.find(node.right))
        #这里由于node.val+left+right一定大于node.val+max(left,right)这种情况，所以省略。
        self.max_num = max(self.max_num,node.val+left+right)
        return node.val+max(left,right)#向上面的父节点递归


# @lc code=end

