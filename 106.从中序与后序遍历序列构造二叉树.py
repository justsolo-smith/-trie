#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder)==0:
            return None
        if len(inorder)==1:
            return TreeNode(inorder[0])

        left_in = inorder[:inorder.index(postorder[-1])]
        right_in = inorder[inorder.index(postorder[-1])+1:]
        left_pos = postorder[:inorder.index(postorder[-1])]
        right_pos = postorder[inorder.index(postorder[-1]):-1]
        
        root = TreeNode(postorder[-1])
        root.right = self.buildTree(right_in,right_pos)
        root.left = self.buildTree(left_in,left_pos)
        
        return root
# @lc code=end

