# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        result = []
        queue = [pRoot]
        while queue:
            res = []
            nextqueue = []
            for i in queue:
                res.append(i.val)
                if i.left:
                    nextqueue.append(i.left)
                if i.right:
                    nextqueue.append(i.right)
            queue = nextqueue
            result.append(res)
        return result