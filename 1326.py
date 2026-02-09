class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        jumps=[0]*(n+1)
        for i,x in enumerate(ranges):
            l,r=max(0,i-x),i+x
            jumps[l]=max(jumps[l],r-l)

        jump=mx=nmx=0
        for i in range(n):
            if nmx<i: return -1
            mx=max(mx,i+jumps[i])
            if i==nmx:
                jump+=1
                nmx=mx

        return jump if nmx>=n else -1

