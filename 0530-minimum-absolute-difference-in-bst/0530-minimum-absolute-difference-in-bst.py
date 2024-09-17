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
        size = len(lst)
        for i in range(size-1):
            if minDif == None:
                minDif = lst[i+1]-lst[i]
            elif lst[i+1]-lst[i] < minDif:
                minDif = lst[i+1]-lst[i]
        return minDif
            