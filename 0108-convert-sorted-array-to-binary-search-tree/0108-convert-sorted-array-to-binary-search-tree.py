# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make_bst(lst):
            n = len(lst)
            if n == 0:
                return None
                
            newNode = TreeNode(lst[n//2])
            lst.remove(lst[n//2])

            newNode.left = make_bst(lst[:n//2])
            newNode.right = make_bst(lst[n//2:])

            return newNode
        
        return make_bst(nums)