#
# @lc app=leetcode.cn id=1028 lang=python3
#
# [1028] 从先序遍历还原二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        ans = {-1: TreeNode(0)}     #字典初始化
        def addTree(v, p):          #添加树函数
            ans[p] = TreeNode(int(v))
            if not ans[p - 1].left: #左子树不存在就加在左边
                ans[p - 1].left = ans[p]
            else:                   #反之加在右边
                ans[p - 1].right = ans[p]
        val, dep = '', 0            #值和对应深度初始化
        for c in S:
            if c != '-':
                val += c            #累加字符来获得数字
            elif val:               #如果是‘-’且存在val
                addTree(val, dep)   #就把累加好的数字和对应深度添加进树
                val, dep = '', 1    #值和对应深度重新初始化
            else:
                dep += 1            #连续的‘-’只加深度不加值
        addTree(val, dep)           #末尾剩余的数字也要加进树
        return ans[0]


        
# @lc code=end

