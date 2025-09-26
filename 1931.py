# class Solution:
#     def colorTheGrid(self, m: int, n: int) -> int:
        
#         poss=[]
#         def backtrack(curr):
#             if len(curr)==m+1: poss.append(curr[1:]);return
#             for k in 'rgb':
#                 if curr[-1]!=k:
#                     backtrack(curr+k)
#         backtrack('#')

#         def canBeNei(a,b):
#             for a,b in zip(a,b):
#                 if a==b: return False
#             return True

#         nei=defaultdict(list)
#         tot=len(poss)
#         for i in range(tot):
#             for j in range(i+1,tot):
#                 a,b=poss[i],poss[j]
#                 if canBeNei(a,b):
#                     nei[a].append(b);nei[b].append(a)

#         nei["#"]=poss
#         mod=10**9+7
#         @cache
#         def helper(prev,j):
#             if j==n: return 1
#             res=0
#             for nxt in nei[prev]:
#                 res=(res+helper(nxt,j+1))%mod
#             return res
#         return helper("#",0)


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        
        q,nei,mod=deque(['r','g','b']),defaultdict(list),10**9+7

        while len(q[0])!=m:
            for _ in range(len(q)):
                c=q.popleft()
                for k in 'rgb':
                    if c[-1]!=k: q.append(c+k)

        tot=len(q)
        nei[-1]=list(range(tot))
        for i in range(tot):
            for j in range(i+1,tot):
                if all(a!=b for a,b in zip(q[i],q[j])):
                    nei[i].append(j);nei[j].append(i)

        @cache
        def helper(prev,j):
            if j==n: return 1
            res=0
            for nxt in nei[prev]: res+=helper(nxt,j+1)
            return res%mod
        return helper(-1,0)

        







