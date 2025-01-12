# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        in_order_list = []

        def in_order(node):
            if not node:
                return
                        
            in_order(node.left)

            in_order_list.append(node.val)
            
            in_order(node.right)
        
        in_order(root)

        for i,ele in enumerate(in_order_list[:-1]):
            if in_order_list[i+1] <= ele:
                return False
        
        return True

            
            