# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return None

        dummy=ListNode(0,head)
        prev,curr=dummy,head

        while curr and curr.next:
            next=curr.next
            nextnext=next.next

            prev.next=next
            next.next=curr
            curr.next=nextnext

            prev,curr=curr,nextnext

        return dummy.next
        