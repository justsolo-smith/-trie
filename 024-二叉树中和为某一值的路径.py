# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    
    def __init__(self):
        self.sumc = 0
        self.a = []
        self.b = []
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        self.sumc += root.val
        self.a.append(root.val)
        if self.sumc == expectNumber and not root.left and not root.right:
            self.b.append(self.a[:])
		#若是有负数的话，则直接改为else
        elif self.sumc < expectNumber:
            self.FindPath(root.left,expectNumber)
            self.FindPath(root.right,expectNumber)
        self.sumc -=self.a[-1]
        self.a.pop()
        return self.b
                