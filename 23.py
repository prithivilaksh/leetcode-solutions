# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
#         h=[]

#         for l in lists:
#             curr=l
#             while curr:
#                 heapq.heappush(h,curr.val)
#                 # todel=curr
#                 curr=curr.next
#                 # del todel
        
#         head=ListNode(-100004)
#         curr=head
#         while h:
#             val=heapq.heappop(h)
#             curr.next=ListNode(val)
#             curr=curr.next
#         return head.next

class Solution(object):
    def mergeKLists(self, lists):
        if not lists: return None
        if len(lists) == 1:return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next