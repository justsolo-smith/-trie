# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        res = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                res = self.same(pRoot1,pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.left, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.right, pRoot2)
        return res
    
    def same(self,root1,root2):
        if not root2:
            return True
        if not root1:
            return False
        return root1.val == root2.val and self.same(root1.left,root2.left) and self.same(root1.right,root2.right)
            
        