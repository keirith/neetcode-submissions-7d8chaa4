# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        nxt = None #initalize starting pointers
        while curr is not None:
            nxt = curr.next #captures nxt
            curr.next = prev #reverses pointer
            prev = curr # moves pointer forward in LL
            curr = nxt #moves pointer forward in LL
        return prev

#Time: O(n) - traversing the LL
#space: O(1) - only utilizing pointers
        