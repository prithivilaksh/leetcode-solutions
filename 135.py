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

# class Solution:
#     def candy(self, rat: List[int]) -> int:
        
#         n=len(rat)
#         indeg=defaultdict(int)
#         g=defaultdict(list)
#         for i in range(n-1):
#             u,v=i,i+1
#             if rat[u]>rat[v]: 
#                 g[v].append(u)
#                 indeg[u]+=1
#             elif rat[v]>rat[u]: 
#                 g[u].append(v)
#                 indeg[v]+=1
        
#         dq,d,res=deque([i for i in range(n) if indeg[i]==0]),1,0
#         while dq:
#             res+=len(dq)*d
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 for v in g[u]:
#                     indeg[v]-=1
#                     if indeg[v]==0: dq.append(v)
#             d+=1
        
#         return res


class Solution:
    def candy(self, rat: List[int]) -> int:
        
        n=len(rat)
        i,res=1,n
        while i<n:
            while i<n and rat[i-1]==rat[i]: i+=1
            upcnt=downcnt=0
            while i<n and rat[i-1]<rat[i]: 
                i+=1
                upcnt+=1
                res+=upcnt
            while i<n and rat[i-1]>rat[i]:
                i+=1
                downcnt+=1
                res+=downcnt
            res-=min(upcnt,downcnt)
        return res



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













