# class Solution:
#     def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:


#         n=len(prices)
#         psum=[0]*n
#         psum[0]=prices[0]*strategy[0]
#         for i in range(1,n):
#             psum[i]=psum[i-1]+(prices[i]*strategy[i])
            
#         res=psum[n-1]
#         rsum=0
#         l,m=0,k//2
#         for r in range(k//2,n):
#             rsum+=1*prices[r]
#             if r>=k:
#                 rsum-=1*prices[m]
#                 rsum+=strategy[l]*prices[l]
#                 m+=1;l+=1
            
#             if r>=k-1: res=max(res,rsum+psum[n-1]-psum[r])

#         return res

class Solution:
    def maxProfit(self, p: List[int], s: List[int], k: int) -> int:

        n=len(p)
        rsum=left=0
        tot=sum([a*b for a,b in zip(p,s)])         
        l,m=0,k//2


        for r in range(k//2):left+=p[r]*s[r]   
        for r in range(k//2,k):left+=p[r]*s[r];rsum+=p[r]
        res=max(tot,rsum+tot-left)
        for r in range(k,n):
            rsum+=(s[l]*p[l])-p[m]+p[r]
            left+=p[r]*s[r]
            res=max(res,rsum+tot-left)
            m+=1;l+=1

        return res