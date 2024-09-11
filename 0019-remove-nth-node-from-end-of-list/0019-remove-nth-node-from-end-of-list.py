# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def lst_to_arr(head,rem_index):
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            arr.pop(-rem_index)
            return arr
        def arr_to_list(arr):
            lst = None
            for i in arr:
                newNode = ListNode(i)
                if lst == None:
                    lst = newNode
                    temp = lst
                else:
                    temp.next = newNode
                    temp = temp.next

            return lst

        return arr_to_list(lst_to_arr(head,n))