# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        curr = head
        prev = None
        n = head.next
        newHead = None

        while curr:
            
            curr.next = prev
            prev = curr

            if n and n.next:
                curr = n
                n = n.next
            else:
                n.next = curr
                curr=None
                newHead = n


        return n