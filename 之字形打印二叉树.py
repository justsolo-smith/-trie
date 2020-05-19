# -*- coding:utf-8 -*-
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
		level = 0
		while len(stack) > 0:
			tmp = []
			new_stack = []
			while len(stack) > 0:
				cur = stack.pop()
				tmp.append(cur.val)
				if level % 2 == 0:
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
			level += 1
		return res