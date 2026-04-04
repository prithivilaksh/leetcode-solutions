# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        mp={}
        it,rsum=dummy,0
        while it:
            rsum+=it.val
            mp[rsum]=it
            it=it.next
        
        it,rsum=dummy,0
        while it:
            rsum+=it.val
            it.next=mp[rsum].next
            it=it.next
        return dummy.next
