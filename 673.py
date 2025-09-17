# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
#         n=len(nums)
#         mx=[1,n]
#         @cache
#         def helper(i):
#             nonlocal mx
#             res=[1,1]#len,cnt
#             for j in range(i+1,n):
#                 if nums[i]<nums[j]:
#                     len,cnt=helper(j)
#                     if len+1>res[0]:res=[len+1,cnt]
#                     elif len+1==res[0]:res[1]+=cnt
#                     if len+1>mx[0]:mx=[len+1,cnt]
#                     elif len+1==mx[0]: mx[1]+=cnt
#             return res
#         for i in range(n):helper(i)
#         return mx[1]



# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
#         n=len(nums)
#         ln,cnt=[1]*n,[1]*n
#         for i in range(n-1,-1,-1):
#             for j in range(i+1,n):
#                 if nums[i]<nums[j]:
#                     if ln[i]<ln[j]+1: ln[i]=ln[j]+1;cnt[i]=cnt[j]
#                     elif ln[i]==ln[j]+1: cnt[i]+=cnt[j]
        
#         l=c=0
#         for i in range(n):
#             if ln[i]>l: l,c=ln[i],cnt[i]
#             elif ln[i]==l: c+=cnt[i]
#         return c

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        x2i={x:i for i,x in enumerate(sorted(set(nums)))}
        n=len(x2i)
        ln,cnt=[0]*(n+1),[0]*(n+1)
        def query(i):
            i+=1
            l=c=0
            while i>=1:
                if ln[i]>l: l,c=ln[i],cnt[i]
                elif ln[i]==l: c+=cnt[i]
                i-=i&-i
            return l,c

        def update(i,l,c):
            i+=1
            while i<=n:
                if ln[i]<l: ln[i],cnt[i]=l,c
                elif ln[i]==l: cnt[i]+=c
                i+=i&-i
        
        for x in nums:
            i=x2i[x]
            l,c=query(i-1)
            update(i,l+1,max(1,c))

        return query(n-1)[1]

# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
        
#         x2i={x:i for i,x in enumerate(sorted(set(nums)))}
#         n=len(x2i)
#         ln,cnt=[0]*4*n,[0]*4*n

#         def query(l,r,i,ql,qr):
#             if r<ql or qr<l: return 0,0
#             if ql<=l and r<=qr: return ln[i],cnt[i]
#             m=l+(r-l)//2
#             ll,lc=query(l,m,2*i+1,ql,qr)
#             rl,rc=query(m+1,r,2*i+2,ql,qr)
#             if ll==rl: return ll,lc+rc
#             return (rl,rc) if ll<rl else (ll,lc)

        
#         def update(l,r,i,pos,pl,pc):
#             if l==r==pos: 
#                 if pl>ln[i]: ln[i],cnt[i]=pl,pc
#                 elif pl==ln[i]: cnt[i]+=pc
#                 return
#             m=l+(r-l)//2
#             if pos<=m: update(l,m,2*i+1,pos,pl,pc)
#             else: update(m+1,r,2*i+2,pos,pl,pc)
#             if ln[2*i+1]==ln[2*i+2]: ln[i],cnt[i]=ln[2*i+1],cnt[2*i+1]+cnt[2*i+2];return
#             ln[i],cnt[i]=(ln[2*i+1],cnt[2*i+1]) if ln[2*i+1]>ln[2*i+2] else (ln[2*i+2],cnt[2*i+2])

#         for x in nums:
#             i=x2i[x]
#             l,c=query(0,n-1,0,0,i-1)
#             update(0,n-1,0,i,l+1,max(1,c))
#         return query(0,n-1,0,0,n-1)[1]
