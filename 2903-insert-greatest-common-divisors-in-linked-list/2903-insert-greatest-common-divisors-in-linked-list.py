# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if b==0:
                return a   
            return gcd(b,a%b)

        if head.next == None:
            return head
        
        temp = head

        while temp.next != None:
            newNode = ListNode(gcd(temp.val,temp.next.val),temp.next)
            temp.next = newNode
            temp = temp.next.next

        return head