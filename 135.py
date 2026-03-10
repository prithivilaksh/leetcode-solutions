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
#     def candy(self, rat: List[int]) -> int:

#         n=len(rat)
#         cand=[0]*n
        
#         for i in sorted(range(n),key=lambda x:rat[x]):
#             mx=0
#             if i-1>=0 and rat[i-1]<rat[i]: mx=max(mx,cand[i-1])
#             if i+1<n and rat[i]>rat[i+1]: mx=max(mx,cand[i+1])
#             cand[i]=mx+1
        
#         return sum(cand)

# class Solution:
#     def candy(self, r: List[int]) -> int:
#         n=len(r)
#         lr,rl=[1]*n,[1]*n
#         for i in range(1,n):
#             if r[i-1]<r[i]:lr[i]=lr[i-1]+1
#         for i in range(n-2,-1,-1):
#             if r[i]>r[i+1]:rl[i]=rl[i+1]+1
#         return sum(max(a,b) for a,b in zip(lr,rl))

# class Solution:
#     def candy(self, r: List[int]) -> int:
#         n=len(r)
#         i,res=1,n
#         while i<n:
#             while i<n and r[i-1]==r[i]:i+=1
#             cnt1=cnt2=0
#             while i<n and r[i-1]<r[i]:
#                 i+=1;cnt1+=1
#                 res+=cnt1
#             while i<n and r[i-1]>r[i]:
#                 i+=1;cnt2+=1
#                 res+=cnt2
#             res-=min(cnt1,cnt2)
#         return res

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1: return 1
        i,candy,n=1,1,len(ratings)
        while (i < n):
            up = down = 0
            while i < n and ratings[i - 1] == ratings[i]:
                candy += 1
                i += 1
            while i < n and ratings[i - 1] < ratings[i]:
                up += 1
                candy += up + 1
                i += 1
            while i < n and ratings[i - 1] > ratings[i]:
                down += 1
                candy += down + 1
                i += 1
            candy -= min(up, down)
        return candy




# class Solution:
#     def candy(self, rat: List[int]) -> int:

#         n=len(rat)
#         cand=[0]*n

#         ix=[(i,x) for i,x in enumerate(rat)]
#         groups=[(k,list(g)) for k,g in groupby(ix,key=lambda x:x[1])]
#         groups.sort(key=lambda x:x[0])        
#         for k,g in groups:
#             next=cand[:]
#             for i,_ in g:
#                 mx=0
#                 if i-1>=0: mx=max(mx,cand[i-1])
#                 if i+1<n: mx=max(mx,cand[i+1])
#                 next[i]=mx+1
#             cand=next
#         return sum(cand)













