# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node1,node2):
            if node1 == None and node2 == None:
                return True
            elif node1 == None or node2 == None:
                return False

            if node1.val != node2.val:
                return False
        
            if not traverse(node1.left,node2.left):
                return False
            if not traverse(node1.right,node2.right):
                return False
            
            return True

        return traverse(p,q)