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


# class Solution:
#     def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
#         def backtrack(i):
#             if i==n:
#                 res[0]=min(res[0],max(time))
#                 return
#             for j in range(k):
#                 if time[j]+jobs[i]>=res[0]: continue
#                 if time[j] in time[:j]: continue
#                 time[j]+=jobs[i]
#                 backtrack(i+1)
#                 time[j]-=jobs[i]
#                 if time[j]==0 : break
        
#         def heuristic():
#             jobs.sort(reverse=True)
#             t=[0]*k
#             for x in jobs:
#                 ind=t.index(min(t))
#                 t[ind]+=x
#             return max(t)

#         n=len(jobs)
#         res,time=[heuristic()],[0]*k
#         backtrack(0)
#         return res[0]

# class Solution:
#     def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
#         def check(tar,jobs):
#             def bt(pos,rem,s):
#                 if rem==1: 
#                     return s+sum(x for x in jobs if x>0)<=tar
#                 for i in range(pos,n):
#                     if jobs[i]<=0 or s+jobs[i]>tar: continue
#                     if i>pos and jobs[i-1]==jobs[i]: continue
#                     jobs[i]=-jobs[i]
#                     if bt(i+1,rem,s+(-jobs[i])): return True
#                     jobs[i]=-jobs[i]
#                     if s==0 or s+jobs[i]==tar: break

#                 return bt(0,rem-1,0)
#             return bt(0,k,0)

#         jobs.sort(reverse=True)
#         l,r,n=max(jobs),sum(jobs),len(jobs)
#         while l<r:
#             m=l+(r-l)//2
#             if check(m,jobs[:]): r=m
#             else: l=m+1
#         return r


# class Solution:
#     def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
#         def check(tar):
#             bucket=[0]*k
#             def bt(pos):
#                 if pos==n: return True
#                 for i in range(k):
#                     if bucket[i] in bucket[:i] or bucket[i]+jobs[pos]>tar: continue
#                     bucket[i]+=jobs[pos]
#                     if bt(pos+1): return True
#                     bucket[i]-=jobs[pos]
#                     if bucket[i]==0 or bucket[i]+jobs[pos]==tar: return False
#             return bt(0)

#         jobs.sort(reverse=True)
#         l,r,n=max(jobs),sum(jobs),len(jobs)
#         while l<r:
#             m=l+(r-l)//2
#             if check(m): r=m
#             else: l=m+1
#         return r

# class Solution:
#     def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
#         def bt(pos):
#             if pos==n: 
#                 res[0]=min(res[0],max(bucket))
#                 return
#             for i in range(k):
#                 if bucket[i] in bucket[:i] or bucket[i]+jobs[pos]>=res[0]: continue
#                 bucket[i]+=jobs[pos]
#                 bt(pos+1)
#                 bucket[i]-=jobs[pos]

#         jobs.sort(reverse=True)
#         bucket,res,n=[0]*k,[inf],len(jobs)
#         bt(0)
#         return res[0]

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
        def bt(pos):
            if pos==n: 
                res[0]=min(res[0],max(bucket))
                return
            for i in range(k):
                if bucket[i] in bucket[:i] or bucket[i]+jobs[pos]>=res[0]: continue
                bucket[i]+=jobs[pos]
                bt(pos+1)
                bucket[i]-=jobs[pos]
                if bucket[i]==0: return

        jobs.sort(reverse=True)
        bucket,n=[0]*k,len(jobs)
        for i in range(n):
            x=bucket.index(min(bucket))
            bucket[x]+=jobs[i]
        bucket,res=[0]*k,[max(bucket)]
        bt(0)
        return res[0]

