# class Solution:
#     def lengthOfLIS(self, nums: List[int], k: int) -> int:
        
#         self.res=1
#         n=len(nums)
#         @cache
#         def helper(pos):
#             if pos==n: return 0
#             helper(pos+1)
#             res=1
#             for j in range(pos+1,n):
#                 if nums[pos]<nums[j]<=nums[pos]+k:
#                     res=max(res,1+helper(j))
#                     self.res=max(self.res,res)
#             return res
#         helper(0)
#         return self.res

# class Solution:
#     def lengthOfLIS(self, nums: List[int], k: int) -> int:
        
#         n=len(nums)
#         dp=[1]*n
#         res=1
        
#         for i in range(n-1,-1,-1):
#             for j in range(i+1,n):
#                 if nums[i]<nums[j]<=nums[i]+k:
#                     dp[i]=max(dp[i],1+dp[j])
#             res=max(res,dp[i])
        
#         return res

# class Solution:
#     def lengthOfLIS(self, nums : List[int], k: int) -> int:
#         n=max(nums)
#         stree=[0]*(4*n)

#         def query(i,l,r,ql,qr):
#             if ql<=l and r<=qr: return stree[i]
#             if r<ql or qr<l: return 0
#             m=l+(r-l)//2
#             return max(query(2*i,l,m,ql,qr),query(2*i+1,m+1,r,ql,qr))
        
#         def update(i,l,r,pos,val):
#             if l==r==pos: stree[i]=max(stree[i],val); return
#             m=l+(r-l)//2
#             if l<=pos<=m: update(2*i,l,m,pos,val)
#             elif m+1<=pos<=r: update(2*i+1,m+1,r,pos,val)
#             stree[i]=max(stree[2*i],stree[2*i+1])
        
#         res=1
#         for x in nums:
#             prevMx=query(1,1,n,max(0,x-k),x-1)
#             res=max(res,prevMx+1)
#             update(1,1,n,x,prevMx+1)
#         return res


class Solution:
    def lengthOfLIS(self, nums : List[int], k: int) -> int:
        n=max(nums)
        stree=[0]*(4*n)

        def query(i,l,r,ql,qr):
            if ql<=l and r<=qr: return stree[i]
            if r<ql or qr<l: return 0
            m=l+(r-l)//2
            return max(query(2*i+1,l,m,ql,qr),query(2*i+2,m+1,r,ql,qr))
        
        def update(i,l,r,pos,val):
            # if r<l: print("something worng")
            if l==r==pos: stree[i]=max(stree[i],val); return
            m=l+(r-l)//2
            if l<=pos<=m: update(2*i+1,l,m,pos,val)
            elif m+1<=pos<=r: update(2*i+2,m+1,r,pos,val)
            stree[i]=max(stree[2*i+1],stree[2*i+2])
        
        res=1
        for x in nums:
            prevMx=query(0,0,n-1,max(0,x-k),x-1)
            res=max(res,prevMx+1)
            update(0,0,n-1,x,prevMx+1)
        return res