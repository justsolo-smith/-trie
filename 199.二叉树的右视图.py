#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = [root]
        result = []
        while queue:
            cur = []
            next_queue = []
            for i in queue:
                cur.append(i.val)
                if i.left:
                    next_queue.append(i.left)
                if i.right:
                    next_queue.append(i.right)
            res.append(cur)
            queue = next_queue
        result = [res[i][-1] for i in range(len(res))]
        return result
# @lc code=end

