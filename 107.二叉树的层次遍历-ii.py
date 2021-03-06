#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            cur = []
            nextqueue = []
            for i in queue:
                cur.append(i.val)
                if i.left:
                    nextqueue.append(i.left)
                if i.right:
                    nextqueue.append(i.right)
            queue = nextqueue
            res.append(cur)
        return res[::-1]

# @lc code=end

