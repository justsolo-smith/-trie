# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
实现一个函数，检查一棵二叉树是否为二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true
'''
#递归遍历
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = root.left
        right = root.right
        while left and left.right:
            left = left.right
        while right and right.left:
            right = right.left
        result = (left is None or left.val < root.val) and (right is None or right.val > root.val)
        return result and self.isValidBST(root.left) and self.isValidBST(root.right)
#中序遍历天然有序
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.res = []
        result = self.midTree(root)
        if len(result)==1:
            return True
        for i in range(len(result)-1):
            if self.res[i] >=self.res[i+1]:
                return False
        return True
    def midTree(self,root):
        if root:
            self.midTree(root.left)
            self.res.append(root.val)
            self.midTree(root.right)
        return self.res

