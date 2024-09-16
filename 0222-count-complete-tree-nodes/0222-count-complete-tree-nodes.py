# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def traverse(node,count):
            if node == None:
                return count
            count += 1

            count = traverse(node.left,count)
            count = traverse(node.right,count)

            return count

        return traverse(root,0)
            