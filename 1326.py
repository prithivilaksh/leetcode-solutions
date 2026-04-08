# class Solution:
#     def minTaps(self, n: int, ranges: List[int]) -> int:
        
#         jumps=[0]*(n+1)
#         for i,x in enumerate(ranges):
#             l,r=max(0,i-x),i+x
#             jumps[l]=max(jumps[l],r-l)

#         jump=mx=nmx=0
#         for i in range(n):
#             if nmx<i: return -1
#             mx=max(mx,i+jumps[i])
#             if i==nmx:
#                 jump+=1
#                 nmx=mx

#         return jump if nmx>=n else -1


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        l2r=defaultdict(int)
        for i,x in enumerate(ranges):
            l,r=max(0,i-x),min(n,i+x)
            l2r[l]=max(l2r[l],r)
        
        taps=cmx=nmx=0
        for i in range(n):
            if i>cmx: return -1
            nmx=max(nmx,l2r[i])
            if i==cmx:
                taps+=1
                cmx=nmx

        return taps if cmx==n else -1
