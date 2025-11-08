# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if not head: return head
#         it=fast=slow=last=head
#         cnt=0
#         while it: last=it;it=it.next;cnt+=1
#         k=k%cnt
#         if k==0: return head

#         for _ in range(k): fast=fast.next

#         while fast.next:
#             fast=fast.next
#             slow=slow.next
        
#         newhead=slow.next
#         slow.next=None
#         last.next=head
#         return newhead

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        it,cnt=head,1
        while it.next: it=it.next;cnt+=1
        k=k%cnt
        it.next=head
        for _ in range(cnt-k): it=it.next

        head=it.next
        it.next=None

        return head