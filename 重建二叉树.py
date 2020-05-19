# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
       # write code here
        if len(pre)==0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        tinl = tin[:tin.index(pre[0])]
        tinr = tin[tin.index(pre[0])+1:]
        root.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1], tinl)
        root.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:], tinr)  
        return root