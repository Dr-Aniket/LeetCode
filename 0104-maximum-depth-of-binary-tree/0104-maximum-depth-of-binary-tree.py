# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            def traverse(node,d):
                if node == None:
                    return None
                
                d += 1

                if d > self.depth:
                    self.depth = d

                traverse(node.left,d)
                traverse(node.right,d)
                               
            traverse(root,0)

            return self.depth