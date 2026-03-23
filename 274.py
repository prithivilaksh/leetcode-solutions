# class Solution:
#     def hIndex(self, cit: List[int]) -> int:
        
#         n=len(cit)
#         l,r=0,n

#         def check(h):
#             cnt=0
#             for x in cit:
#                 cnt+=x>=h
#             return cnt>=h

#         res=0
#         while l<=r:
#             m=l+(r-l)//2
#             if check(m): res,l=m,m+1
#             else: r=m-1
#         return res

# class Solution:
#     def hIndex(self, cit: List[int]) -> int:
        
#         n=len(cit)
#         bucket=[0]*1001
#         for x in cit:
#             bucket[x]+=1
        
#         rcnt=0
#         for i in range(1000,-1,-1):
#             rcnt+=bucket[i]
#             if rcnt>=i: return i

class Solution:
    def hIndex(self, cit: List[int]) -> int:
        
        n=min(len(cit),1000)
        bucket=[0]*(n+1)
        for x in cit:
            bucket[min(n,x)]+=1
        
        rcnt=0
        for i in range(n,-1,-1):
            rcnt+=bucket[i]
            if rcnt>=i: return i