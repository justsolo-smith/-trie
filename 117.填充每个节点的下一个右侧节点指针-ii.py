# @before-stub-for-debug-begin
from python3problem117 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
'''
#非完全二叉树
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def helper(root):
            while root.next:
                if root.next.left:
                    return root.next.left
                elif root.next.right:
                    return root.next.right
                root = root.next
            return None
        if not root or (not root.left and not root.right):
            return root
        if root.left and root.right:
            root.left.next = root.right
            root.right.next = helper(root)
        if root.left and not root.right:
            root.left.next = helper(root)
        if root.right and not root.left:
            root.right.next = helper(root)
        #先递归右子树再递归左子树，因为有右才有左！！！
        self.connect(root.right)
        self.connect(root.left)
        return root
  
# @lc code=end

