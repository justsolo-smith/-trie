#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        left_pre = preorder[1:inorder.index(preorder[0])+1]
        right_pre = preorder[inorder.index(preorder[0])+1:]
        left_in = inorder[:inorder.index(preorder[0])]
        right_in = inorder[inorder.index(preorder[0])+1:]

        root = TreeNode(preorder[0])
        root.left = self.buildTree(left_pre,left_in)
        root.right = self.buildTree(right_pre,right_in)
        return root
# @lc code=end

