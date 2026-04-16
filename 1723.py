# class Solution:
#     def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
#         def backtrack(i):
#             if i==n:
#                 res[0]=min(res[0],max(time))
#                 return
#             vis=set()
#             for j in range(k):
#                 if time[j]+jobs[i]>res[0]: continue
#                 if time[j] in vis: continue
#                 vis.add(time[j])
#                 time[j]+=jobs[i]
#                 backtrack(i+1)
#                 time[j]-=jobs[i]
        
#         n=len(jobs)
#         res,time=[inf],[0]*k
#         backtrack(0)
#         return res[0]

# class Solution:
#     def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
#         def backtrack(i):
#             if i==n: return True
#             for j in range(k):
#                 if time[j]+jobs[i]>m: continue
#                 if time[j] in time[:j]: continue
#                 time[j]+=jobs[i]
#                 if backtrack(i+1): return True
#                 time[j]-=jobs[i]
#                 if time[j]==0 or time[j]+jobs[i]==m: break
#             return False
#         n=len(jobs)
#         jobs.sort(reverse=True)
#         l,r=max(jobs),sum(jobs)
#         while l<r:
#             m=l+(r-l)//2
#             time=[0]*k
#             if backtrack(0): r=m
#             else: l=m+1
#         return r


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
        def backtrack(i):
            if i==n:
                res[0]=min(res[0],max(time))
                return
            for j in range(k):
                if time[j]+jobs[i]>=res[0]: continue
                if time[j] in time[:j]: continue
                time[j]+=jobs[i]
                backtrack(i+1)
                time[j]-=jobs[i]
                if time[j]==0 : break
        
        def heuristic():
            jobs.sort(reverse=True)
            t=[0]*k
            for x in jobs:
                ind=t.index(min(t))
                t[ind]+=x
            return max(t)

        n=len(jobs)
        res,time=[heuristic()],[0]*k
        backtrack(0)
        return res[0]