#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 层次遍历思想，栈实现逆序，精妙
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]
        flag = 0
        while stack:
            tmp = []
            new_stack = []
            while stack:
                #精华，栈是逆序，所以就有了逆逆为正，正逆为逆。
                cur = stack.pop()
                tmp.append(cur.val)
                if flag ==0:
                    if cur.left:
                        new_stack.append(cur.left)
                    if cur.right:
                        new_stack.append(cur.right)
                else:
                    if cur.right:
                        new_stack.append(cur.right)
                    if cur.left:
                        new_stack.append(cur.left)
            res.append(tmp)
            stack = new_stack
            flag = 1-flag
        return res

# @lc code=end

