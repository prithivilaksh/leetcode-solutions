# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         dummy=ListNode(0)
#         it,c=dummy,0
#         while l1 or l2:
#             if l1 and l2:

#                 s=l1.val+l2.val+c
#                 if s>=10: s-=10;c=1
#                 else: c=0

#                 l1.val=s
#                 it.next=l1

#                 l1=l1.next
#                 l2=l2.next
                
#             elif l1: 
#                 s=l1.val+c
#                 if s>=10: s-=10;c=1
#                 else: c=0

#                 l1.val=s
#                 it.next=l1

#                 l1=l1.next
#             elif l2: 
#                 s=l2.val+c
#                 if s>=10: s-=10;c=1
#                 else: c=0

#                 l2.val=s
#                 it.next=l2

#                 l2=l2.next

#             it=it.next
#         if c: it.next=ListNode(c)

#         return dummy.next


# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         dummy=ListNode(0)
#         it,c=dummy,0
#         while l1 or l2:
#             s=c
#             if l1: s+=l1.val
#             if l2: s+=l2.val
#             if s>=10: s-=10;c=1
#             else: c=0

#             if l1: next=l1
#             else: next=l2
#             next.val=s

#             it.next=next

#             it=it.next
#             if l1: l1=l1.next
#             if l2: l2=l2.next

#         if c: it.next=ListNode(c)

#         return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode(0)
        it,s=dummy,0
        while l1 or l2 or s:
            if l1: s+=l1.val;l1=l1.next
            if l2: s+=l2.val;l2=l2.next
            it.next=ListNode(s%10)
            s=s//10
            it=it.next

        return dummy.next