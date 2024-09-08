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
                    return d
                
                d += 1

                d1 = traverse(node.left,d)
                d2 = traverse(node.right,d)
                    
                return max(d1,d2)

            d = traverse(root,0)

            return d