# class Solution:
#     def canTransform(self, start: str, result: str) -> bool:
        
#         # idea
#         # - R can move right and L can move left against X
#         # - count from left to right
#         #     - add 1 for start
#         #     - sub 1 for result
#         #     - L count should be -ve at any point
#         #     - R count should be +ve at any point
#         #     - If both L is -ve and R is +ve then its not possible

#         # XXXLRXXXX
#         # LXXXXRXXX

#         # XXR
#         # LXX

#         # RXX
#         # XXL

#         cnt=defaultdict(int)
#         for a,b in zip(start,result):
#             cnt[a]+=1
#             if cnt["L"]!=0 and cnt["R"]!=0: return False
#             cnt[b]-=1
#             if cnt["L"]!=0 and cnt["R"]!=0: return False

#             if cnt["L"]>0 or cnt["R"]<0: return False

#         return cnt["L"]==cnt["R"]==cnt["X"]==0


class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        
        n=len(start)
        i=j=0
        while True:
            while i<n and start[i]=='X': i+=1
            while j<n and result[j]=='X': j+=1

            if i==n and j==n: return True
            if i==n or j==n: return False
            if start[i]!=result[j]: return False
            if start[i]=='L' and i<j: return False
            if start[i]=='R' and j<i: return False

            i+=1;j+=1
