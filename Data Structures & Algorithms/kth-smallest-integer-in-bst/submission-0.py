# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
            res.append(node.val)
            # if len(res) == k:
            #     return
            
            if node.right:
                dfs(node.right)
            # if k == 0:
            #     return node.val
            # if node.left:
            #     dfs(node.left, k-1)
            # elif node.right:
            #     dfs(node.right, k-1)


        dfs(root)
        return res[k-1]
        