# class Solution:
#     def trap(self, h: List[int]) -> int:
        
#         n=len(h)
#         lr,rl=[0]*n,[0]*n

#         lr[0]=h[0]
#         for i in range(1,n):
#             lr[i]=max(lr[i-1],h[i])
        
#         rl[n-1]=h[n-1]
#         for i in range(n-2,-1,-1):
#             rl[i]=max(rl[i+1],h[i])
        
#         res=0
#         for i in range(n):
#             res+=min(lr[i],rl[i])-h[i]
        
#         return res


# class Solution:
#     def trap(self, h: List[int]) -> int:
        
#         n=len(h)
#         st=[]
#         res=0
#         for r in range(n):
#             while st and h[st[-1]]<=h[r]:
#                 m=st.pop()
#                 if not st: break
#                 l=st[-1]
#                 res+=(r-l-1)*(min(h[l],h[r])-h[m])
#             st.append(r)
        
#         return res

class Solution:
    def trap(self, h: List[int]) -> int:
        
        l,r=0,len(h)-1
        res=lmax=rmax=0
        while l<=r:
            lmax=max(lmax,h[l])
            rmax=max(rmax,h[r])

            if lmax<=rmax:
                res+=lmax-h[l]
                l+=1
            else:
                res+=rmax-h[r]
                r-=1
        return res
        
