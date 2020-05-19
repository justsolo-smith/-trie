#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return res
        
# @lc code=end

