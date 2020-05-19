'''
给定二叉树的根节点 root，找出存在于不同节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。

（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return None
        self.res = 0
        self.search(root,root.val,root.val)
        return self.res

    def search(self,root,maxroot,minroot):
        if not root:
            return
        self.res = max(self.res,max(abs(maxroot-root.val),abs(minroot-root.val)))
        if maxroot < root.val:
            maxroot = root.val
        if minroot > root.val:
            minroot = root.val
        self.search(root.left,maxroot,minroot)
        self.search(root.right,maxroot,minroot)
        return maxroot,minroot