# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
        
#         arr=[]
#         n=len(nums)
#         for i in range(n-1,-1,-1):
#             pos=bisect_left(arr,nums[i])
#             arr.insert(pos,nums[i])
#             nums[i]=pos

#         return nums

# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
        
#         n=len(nums)
#         nums=[(x,i) for i,x in enumerate(nums)]
#         res=[0]*n

#         def divideMerge(l,r):
#             if l==r: return 
#             m=l+(r-l)//2
#             divideMerge(l,m)
#             divideMerge(m+1,r)
#             merge(l,m,m+1,r)

#         def merge(l1,r1,l2,r2):
#             i,j=l1,l2
#             tmp=[]
#             while i<=r1 or j<=r2:
#                 if j>r2 or i<=r1 and nums[i][0]<=nums[j][0]: 
#                     res[nums[i][1]]+=j-l2
#                     tmp.append(nums[i]);i+=1
#                 else: tmp.append(nums[j]);j+=1

#             nums[l1:r2+1]=tmp[:]
        
#         divideMerge(0,n-1)

#         return res

# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
        
#         numset=sorted(set(nums))
#         nToi={}
#         for i,x in enumerate(numset): nToi[x]=i
#         N=len(numset)
#         stree=[0]*2*N

#         def update(i,val):
#             i+=N
#             stree[i]+=val
#             while i>1:
#                 i//=2
#                 stree[i]=stree[2*i]+stree[2*i+1]
        
#         def query(l,r):
#             l+=N
#             r+=N
#             cnt=0
#             while l<r:
#                 if l&1:
#                     cnt+=stree[l]
#                     l+=1
#                 if r&1:
#                     r-=1
#                     cnt+=stree[r]
#                 l//=2;r//=2
#             return cnt
        
#         n=len(nums)
#         for i in range(n-1,-1,-1):
#             ind=nToi[nums[i]]
#             nums[i]=query(0,ind)
#             update(ind,1)
#         return nums



class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        numset=sorted(set(nums))
        nToi={}
        for i,x in enumerate(numset): nToi[x]=i
        N=len(numset)+1
        f=[0]*N

        def update(i,val):
            i+=1
            while i<N:
                f[i]+=val
                i+=i&-i
        
        def query(i):
            i+=1
            cnt=0
            while i>0:
                cnt+=f[i]
                i-=i&-i
            return cnt
        
        n=len(nums)
        for i in range(n-1,-1,-1):
            ind=nToi[nums[i]]
            nums[i]=query(ind-1)
            update(ind,1)
        return nums
