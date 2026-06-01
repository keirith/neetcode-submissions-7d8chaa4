# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        nxt = None
        while curr is not None:
            nxt = curr.next #hold curr.next
            curr.next = prev #reverses pointer
            prev = curr #moves pointer forward
            curr = nxt #moves pointer forward

        return prev #will land at tail of old ll, new head.
        #Time: O(n) - traversing linkedlist
        #Space: O(1) - pointer manipulation
        
#.  None <- A    B -> C
#.          p    c.   n