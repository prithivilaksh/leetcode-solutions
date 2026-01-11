# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         fast=slow=head
#         while fast.next and fast.next.next:
#             fast=fast.next.next
#             slow=slow.next
        
#         prev,curr=None,slow.next
#         slow.next=None
#         while curr:
#             next=curr.next
#             curr.next=prev
#             prev=curr
#             curr=next
        
#         dummy=ListNode(0)
#         h1,h2=head,prev
#         it=dummy
#         while h2:
#             it.next=h1
#             h1=h1.next
#             it=it.next
#             it.next=h2
#             h2=h2.next
#             it=it.next
#         if h1: it.next=h1

#         return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        prev,curr=None,slow.next
        slow.next=None
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        
        h1,h2=head,prev
        while h1:
            next=h1.next
            h1.next=h2
            h1=h1.next
            h2=next

        return head

        