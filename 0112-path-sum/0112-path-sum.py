# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        paths = []
        path = []

        def dfs(node):
            if not node:
                return 
            
            path.append(node.val)
        
            if node.left == None and node.right == None:
                paths.append(sum(path) == targetSum)
            else:
                dfs(node.left)
                dfs(node.right)
            
            path.pop()
        
        dfs(root)

        return any(paths)

                