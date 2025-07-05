# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        
#         nhead=Node(0)
#         otoi,itoo={},{}

#         ind,curr=0,head
#         while curr:
#             otoi[curr]=ind

#             ind+=1
#             curr=curr.next

#         ind,curr,ncurr=0,head,nhead
#         while curr:
#             ncurr.next=Node(curr.val)
#             itoo[ind]=ncurr.next

#             ind+=1
#             ncurr=ncurr.next
#             curr=curr.next
        
#         curr,ncurr=head,nhead.next
#         while curr:
#             rind=otoi.get(curr.random,-1)
#             ncurr.random=itoo.get(rind,None)

#             ncurr=ncurr.next
#             curr=curr.next


#         return nhead.next



"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        
        mp={}
        curr=head
        while curr:
            mp[curr]=Node(curr.val)
            curr=curr.next
        
        curr=head
        while curr:
            mp[curr].next=mp.get(curr.next)
            mp[curr].random=mp.get(curr.random)
            curr=curr.next
        
        return mp.get(head)