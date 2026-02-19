# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if k==1 or not head or not head.next: return head

#         curr=head
#         cnt=0        
#         while curr and cnt<k:
#             cnt+=1
#             curr=curr.next
#         if cnt<k: return head

#         curr=head
#         prev=None
#         while curr and cnt:
#             next=curr.next
#             curr.next=prev
#             prev=curr
#             curr=next
#             cnt-=1
        
#         head.next=self.reverseKGroup(curr,k)
#         return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if k==1: return head

#         curr=head
#         cnt=0        
#         while curr and cnt<k:
#             cnt+=1
#             curr=curr.next
#         if cnt<k: return head

#         curr=head
#         prev=None
#         while curr and cnt:
#             curr.next,curr,prev=prev,curr.next,curr
#             cnt-=1
        
#         head.next=self.reverseKGroup(curr,k)
#         return prev

# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if k==1 or not head or not head.next: return head

#         curr=head
#         for _ in range(k):
#             if not curr: return head
#             curr=curr.next

#         prev,curr=None,head
#         for _ in range(k):
#             next=curr.next
#             curr.next=prev
#             prev=curr
#             curr=next
        
#         head.next=self.reverseKGroup(curr,k)
#         return prev

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr=head
        for _ in range(k):
            if not curr: return head
            curr=curr.next

        prev,curr=None,head
        for _ in range(k):
            next=curr.next
            curr.next=prev
            prev,curr=curr,next
        
        head.next=self.reverseKGroup(curr,k)
        return prev




























