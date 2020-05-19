# @before-stub-for-debug-begin
from python3problem114 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
给定一个二叉树，原地将它展开为一个单链表。

 

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''
'''
    1
   / \
  2   3
将右节点挂到左节点的最右边
    1
   / 
  2   
   \   
    3   
再将整个左子树挂到根节点的右边，这样就可以将整棵树变成链表结构了。
    1
     \
      2
       \
        3
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        #后序遍历
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            #找到左子树的最右边节点
            pre = root.left
            while pre.right:
                pre = pre.right
            #将右节点挂在左子树的最右边节点上
            pre.right = root.right
            #再将整个左子树挂在根节点的右边
            root.right = root.left
            root.left = None
      
# @lc code=end

