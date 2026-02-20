# class Solution:
#     def maximumRobots(self, ct: List[int], rc: List[int], budget: int) -> int:
        

#         n=len(ct)
#         def check(k):

#             dq,rsum=deque(),0
#             for i in range(n):
#                 while dq and dq[0]<=i-k: dq.popleft()
#                 while dq and ct[dq[-1]]<=ct[i]: dq.pop()
#                 dq.append(i)
#                 rsum+=rc[i]
#                 if i<k-1: continue
#                 if i>=k: rsum-=rc[i-k]
#                 if ct[dq[0]]+k*rsum<=budget: return True

#             return False


#         l,r,res=0,n,0
#         while l<=r:
#             m=l+(r-l)//2
#             if check(m): res,l=m,m+1
#             else: r=m-1

#         return res


# class Solution:
#     def maximumRobots(self, ct: List[int], rc: List[int], budget: int) -> int:
        

#         n=len(ct)
#         def check(k):

#             dq,rsum,cnt=deque(),0,0
#             for i in range(n):
#                 while dq and dq[0]<=i-k: dq.popleft()
#                 while dq and ct[dq[-1]]<=ct[i]: dq.pop()
#                 dq.append(i)
#                 rsum+=rc[i]
#                 cnt+=1
#                 if cnt<k: continue
#                 if cnt>k: rsum-=rc[i-k]
#                 if ct[dq[0]]+k*rsum<=budget: return True

#             return False


#         l,r,res=0,n,0
#         while l<=r:
#             m=l+(r-l)//2
#             if check(m): res,l=m,m+1
#             else: r=m-1

#         return res



# class Solution:
#     def maximumRobots(self, ct: List[int], rc: List[int], budget: int) -> int:
        

#         n,res,rsum,l=len(ct),0,0,0
#         dq=deque()

#         for r in range(n):
#             while dq and ct[dq[-1]]<=ct[r]: dq.pop()
#             dq.append(r)
#             rsum+=rc[r]
#             while dq and ct[dq[0]] + (r-l+1) * rsum  > budget:
#                 if l==dq[0]: dq.popleft()
#                 rsum-=rc[l]
#                 l+=1
#             res=max(res,r-l+1)
#         return res

class Solution:
    def maximumRobots(self, ct: List[int], rc: List[int], budget: int) -> int:
        

        n,res,rsum,l=len(ct),0,0,0
        dq=deque()

        for r in range(n):
            while dq and ct[dq[-1]]<=ct[r]: dq.pop()
            dq.append(r)
            rsum+=rc[r]
            if ct[dq[0]] + (r-l+1) * rsum  > budget:
                if l==dq[0]: dq.popleft()
                rsum-=rc[l]
                l+=1

        return r-l+1














