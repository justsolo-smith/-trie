# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return None
        left = []
        right = []
        num = 0
        for i in range(len(sequence)):
            if sequence[i] < sequence[-1]:
                left.append(sequence[i])
            else:
                num = i
                break
        for j in range(num,len(sequence)-1):
            if sequence[j] > sequence[-1]:
                right.append(sequence[j])
            else:
                return False
        self.VerifySquenceOfBST(left)
        self.VerifySquenceOfBST(right)
        return True