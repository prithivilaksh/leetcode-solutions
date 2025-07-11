# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next: return head

#         slow=head
#         fast=head.next
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next

#         mid=slow.next
#         slow.next=None

#         l=self.sortList(head)
#         r=self.sortList(mid)

#         head=curr=ListNode()
#         while l and r:
#             if l.val<=r.val:
#                 curr.next=l
#                 l=l.next
#             else:
#                 curr.next=r
#                 r=r.next
#             curr=curr.next
#         curr.next=l or r

#         return head.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def splitANext(head,width):
            curr=head
            width-=1
            while curr and width:
                curr=curr.next
                width-=1

            if not curr : return None
            next=curr.next
            curr.next=None
            return next
        
        def mergeATail(prevTail,l,r):
            curr=prevTail
            while l and r:
                if l.val<=r.val:
                    curr.next=l
                    l=l.next
                else:
                    curr.next=r
                    r=r.next
                curr=curr.next
            curr.next=l or r
            while curr.next: curr=curr.next
            return curr

        length,curr=0,head
        while curr:
            length+=1
            curr=curr.next

        width=1
        dummy=ListNode(-1,head)
        while width<length:
            prevTail=dummy
            rem=dummy.next
            while rem:
                left=rem
                right=splitANext(left,width)
                rem=splitANext(right,width)
                prevTail=mergeATail(prevTail,left,right)
            width*=2
        
        return dummy.next

