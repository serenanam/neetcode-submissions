# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(node, maxVal):
            if not node:
                return 0
            cnt = 0
            if node.val >= maxVal:
                cnt = 1
                maxVal = node.val
                # maxVal = max(maxVal, node.val)
            return dfs(node.left, maxVal) + dfs(node.right, maxVal) + cnt
            
        return dfs(root, root.val)
        