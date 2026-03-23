# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, t: int) -> List[int]:
        
#         dq=deque([])
#         for x in arr:
#             dq.append(x)
#             if len(dq)>k:
#                 if abs(dq[0]-t) > abs(dq[-1]-t): dq.popleft()
#                 else: dq.pop()
#         return list(dq)


# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
#         l,r=0,len(arr)-k

#         while l<r:
#             m=l+(r-l)//2
#             if x-arr[m]<=arr[m+k]-x:r=m
#             else: l=m+1
#         return arr[r:r+k]


# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
#         n=len(arr)
#         l,r=0,n-1

#         while l<=r:
#             m=l+(r-l)//2
#             if arr[m]==x: break
#             elif arr[m]<x: l=m+1
#             else: r=m-1
        
#         l=r=m

#         while r-l-1<k:
#             if l==-1: r+=1
#             elif r==n: l-=1
#             elif x-arr[l]<=arr[r]-x: l-=1
#             else: r+=1
#         return arr[l+1:r]


# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
#         n=len(arr)
#         l,r=0,n-1

#         while l<r:
#             m=l+(r-l)//2
#             if arr[m]>=x: r=m
#             else: l=m+1
        
#         l=r

#         while r-l-1<k:
#             if l==-1: r+=1
#             elif r==n: l-=1
#             elif abs(x-arr[l])<=abs(arr[r]-x): l-=1
#             else: r+=1
#         return arr[l+1:r]



class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        n=len(arr)
        l,r=0,n-1

        while l<r:
            m=l+(r-l)//2
            if arr[m]>=x: r=m
            else: l=m+1
        
        l=r

        while r-l-1<k:
            if l==-1: r+=1
            elif r==n: l-=1
            elif x-arr[l]<=arr[r]-x: l-=1
            else: r+=1
        return arr[l+1:r]


# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, y: int) -> List[int]:
        
#         dq=deque()
#         for x in arr:
#             dq.append(x)
#             if len(dq)<=k: continue
#             if abs(dq[0]-y)<=abs(dq[-1]-y): dq.pop()
#             else: dq.popleft()
        
#         return list(dq)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        n=len(arr)
        l,r=0,n-1-k+1
        while l<r:
            m=l+(r-l)//2
            if x-arr[m]<=arr[m+k]-x: r=m
            else: l=m+1
        return arr[r:r+k]



# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
#         n=len(arr)
#         pos=bisect_left(arr,x)
#         nl,nr=pos-1,pos
#         for _ in range(k):
#             if nl==-1: nr+=1
#             elif nr==n: nl-=1
#             elif abs(arr[nl]-x)<=abs(arr[nr]-x): nl-=1
#             else: nr+=1
#         return arr[nl+1:nr]


# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

#         n=len(arr)
#         l,r,res=0,n-1-k+1,0
#         while l<=r:
#             m=l+(r-l)//2
#             if m+k==n: break
#             if x-arr[m]<=arr[m+k]-x:
#                 res=m
#                 r=m-1
#             else:
#                 res=l=m+1

#         return arr[res:res+k]


# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

#         n=len(arr)
#         l,r,res=0,n-1-k+1,n-1-k+1
#         while l<=r:
#             m=l+(r-l)//2
#             if m+k==n: break
#             if x-arr[m]<=arr[m+k]-x:
#                 res=m
#                 r=m-1
#             else:
#                 l=m+1

#         return arr[res:res+k]



# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

#         n=len(arr)
#         l,r,res=0,n-1-k+1,n-1-k+1
#         while l<r:
#             m=l+(r-l)//2
#             if x-arr[m]<=arr[m+k]-x:
#                 res=m
#                 r=m
#             else:
#                 l=m+1

#         return arr[r:r+k]
