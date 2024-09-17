# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst = []
        def traverse(node):
            if node == None:
                return
            minDif = traverse(node.left)
            lst.append(node.val)
            minDif = traverse(node.right)
        
        traverse(root)
        minDif = None
        l1,l2 = lst[:-1],lst[1:]
        for i,j in zip(l1,l2):
            if minDif == None:
                minDif = j-i
            elif j-i < minDif:
                minDif = j-i
        return minDif
            