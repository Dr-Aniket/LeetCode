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
                if sum(path) == targetSum:
                    return True
            else:
                if dfs(node.left):
                    return True
                if dfs(node.right):
                    return True
                                
            path.pop()
        
        return dfs(root)
        
                