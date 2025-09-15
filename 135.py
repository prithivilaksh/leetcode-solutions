# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         h=[(r,i) for i,r in enumerate(ratings)]
#         heapify(h)
#         n=len(h)
#         res=[0]*n
#         while h:
#             r,i=heappop(h)
#             candies=0
#             if i-1>=0 and ratings[i-1]<r: candies=max(candies,res[i-1])
#             if i+1<n  and ratings[i+1]<r: candies=max(candies,res[i+1])
#             res[i]=candies+1
#         return sum(res)

# class Solution:
#     def candy(self, r: List[int]) -> int:
#         n=len(r)
#         lr,rl=[1]*n,[1]*n
#         for i in range(1,n):
#             if r[i-1]<r[i]:lr[i]=lr[i-1]+1
#         for i in range(n-2,-1,-1):
#             if r[i]>r[i+1]:rl[i]=rl[i+1]+1
#         return sum(max(a,b) for a,b in zip(lr,rl))

class Solution:
    def candy(self, r: List[int]) -> int:
        n=len(r)
        i,res=1,n
        while i<n:
            while i<n and r[i-1]==r[i]:i+=1
            cnt1=cnt2=0
            while i<n and r[i-1]<r[i]:
                i+=1;cnt1+=1
                res+=cnt1
            while i<n and r[i-1]>r[i]:
                i+=1;cnt2+=1
                res+=cnt2
            res-=min(cnt1,cnt2)
        return res