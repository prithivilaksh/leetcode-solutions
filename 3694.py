# class Solution:
#     def distinctPoints(self, s: str, k: int) -> int:

#         x=y=0

#         def update(i,sign=1):
#             nonlocal x,y
#             if s[i]=='U': y+=1*sign
#             elif s[i]=='D': y-=1*sign
#             elif s[i]=='L': x-=1*sign
#             else: x+=1*sign
                
#         for i,_ in enumerate(s): update(i)

#         l,res=0,set()
#         for r,c in enumerate(s):
#             if r>=k: update(l,-1);l+=1
#             update(r)
#             if r>=k-1: res.add((x,y))
                
#         return len(res)

# class Solution:
#     def distinctPoints(self, s: str, k: int) -> int:

#         x=y=0

#         def update(i,sign=1):
#             nonlocal x,y
#             if s[i]=='U': y+=1*sign
#             elif s[i]=='D': y-=1*sign
#             elif s[i]=='L': x-=1*sign
#             else: x+=1*sign
                
#         l,res=0,set()
#         for r,c in enumerate(s):
#             if r>=k: update(l,-1);l+=1
#             update(r)
#             if r>=k-1: res.add((x,y))
                
#         return len(res)

class Solution:
    def distinctPoints(self, s: str, k: int) -> int:

        x=y=0
        def update(i,sign=1):
            nonlocal x,y
            if s[i]=='U': y+=sign
            elif s[i]=='D': y-=sign
            elif s[i]=='L': x-=sign
            elif s[i]=='R': x+=sign
                
        n,res=len(s),{(0,0)}
        for r in range(k,n):
            update(r-k,-1)
            update(r)
            res.add((x,y))

        return len(res)