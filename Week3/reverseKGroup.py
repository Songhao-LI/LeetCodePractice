# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # the number of rest elements > k ?
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        dummy = ListNode(0, head)
        p0 = dummy
        prev = None
        curr = p0.next
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt

            nxt = p0.next
            p0.next.next = curr
            p0.next = prev
            p0 = nxt

        return dummy.next
