

# class Solution:
#     def minTime(self, s: str, order: List[int], k: int) -> int:

#         n,res=len(s),0
#         def isValid(t):
#             x=list(s)
#             for i in range(t+1):
#                 x[order[i]]="*"
            
#             pos,res=-1,0
#             for i in range(n):
#                 if x[i]=="*":pos=i
#                 res+=pos+1
#                 if res>=k: return True
#             return False
        
#         l,r,res=0,n-1,-1
#         while l<=r:
#             m=l+(r-l)//2
#             if isValid(m):r=m-1;res=m
#             else: l=m+1
#         return res




class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:

        n,res=len(s),0
        vis=[-1,n]
        for i,o in enumerate(order):
            pos=bisect.bisect(vis,o)
            vis.insert(pos,o)
            l,r=pos-1,pos+1
            res+=(vis[pos]-vis[pos-1])*(vis[pos+1]-vis[pos])
            if res>=k: return i

        return -1

# class Solution:
#     def minTime(self, s: str, order: List[int], k: int) -> int:
#         pos = SortedList([-1, len(s)])
#         for t, i in enumerate(order):
#             j = pos.bisect(i)
#             k -= (i - pos[j - 1]) * (pos[j] - i)
#             pos.add(i)
#             if k <= 0:
#                 return t
#         return -1