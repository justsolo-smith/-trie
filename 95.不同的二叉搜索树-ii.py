# @before-stub-for-debug-begin
from python3problem95 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start > end:
                return [None,]
            
            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)
                
                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)
                
                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            
            return all_trees
        
        return generate_trees(1, n) if n else []

class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return None
        # 对dp进行初始化
        dp = []
        for i in range(0, n+1):   # 初始化dp
            dp.append([])
            for j in range(0, n+1):
                if i == j:
                    dp[i].append([TreeNode(i)])
                elif i < j:
                    dp[i].append([])
                else:
                    dp[i].append([None])
        dp[0][0] = [None]
        for i in range(n-1, 0, -1):  # 自下向上进行循环
            for j in range(i+1, n+1):
                for r in range(i, j+1):   # i-j每一个节点为顶点的情况
                    left = r+1 if r < j else r    # 右边的值需要边界判断，不然会溢出数组
                    for x in dp[i][r-1]:          # 左右子树排列组合   
                        for y in dp[left][j]:
                            node = TreeNode(r)     
                            node.left = x
                            node.right = y
                            if r == j:
                                node.right = None
                            dp[i][j].append(node)      # dp[i][j]添加此次循环的值
        return dp[1][n]



# @lc code=end

