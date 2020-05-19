# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:
            right = pNode.right
            while right.left:
                right =right.left
            return right
        else:
            while pNode.next:
                if pNode.next.left == pNode:
                    return pNode.next
                else:
                    pNode = pNode.next
            return None
            
                
                
                
                