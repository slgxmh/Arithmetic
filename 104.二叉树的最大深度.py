#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.depth(0, root)

    def depth(self, depth: int, n: TreeNode) -> int:
        if n == None:
            return depth
        leftDepth = self.depth(depth + 1, n.left)
        rightDepth = self.depth(depth + 1, n.right)
        return max(leftDepth, rightDepth)


# @lc code=end
