# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def insert_val(head,val):
            newNode = ListNode(val)
            if not head:
                head = newNode
            else:
                temp = head
                while temp.next:
                    temp = temp.next
                temp.next = newNode
            
            return head
        
        def arr_to_list(arr):
            head = None
            for i in arr:
                head = insert_val(head,i)
            
            return head

        def list_to_arr(head):
            arr = []
            temp = head
            if not temp:
                return arr
            while temp:
                arr.append(temp.val)
                temp = temp.next
            
            return arr
            
        return arr_to_list(sorted(list_to_arr(list1)+list_to_arr(list2)))