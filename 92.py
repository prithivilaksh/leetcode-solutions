# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        prev,curr=dummy,head
        for _ in range(l-1):
            prev=curr
            curr=curr.next
        end=prev
        
        prev=None
        mhead=curr
        for _ in range(r-l+1):
            curr.next,prev,curr=prev,curr,curr.next
        
        mhead.next=curr
        end.next=prev
        return dummy.next