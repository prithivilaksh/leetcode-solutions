# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
        
#         cnt=defaultdict(int)
#         for t in tasks: cnt[t]+=1

#         htime=[(1,c,id) for id,c in cnt.items()]
#         heapify(htime)
#         hcnt=[]

#         time=1
#         while htime or hcnt:

#             while htime and htime[0][0]<=time:
#                 t,c,id=heappop(htime)
#                 heappush(hcnt,(-c,id))
            
#             if hcnt:
#                 c,id=heappop(hcnt)
#                 c=-c
#                 c-=1
#                 if c: heappush(htime,(time+n+1,c,id))
#                 time+=1
#             else:
#                 time,c,id=heappop(htime)
#                 c-=1
#                 if c: heappush(htime,(time+n+1,c,id))
#                 time+=1
            
#         return time-1


        
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
        
#         cnt=Counter(tasks)
#         htime,hcnt=[(1,c) for c in cnt.values()],[]
#         time=1
#         while htime or hcnt:

#             while htime and htime[0][0]<=time:
#                 t,c=heappop(htime)
#                 heappush(hcnt,-c)
            
#             if hcnt: c=-heappop(hcnt)
#             else: time,c=heappop(htime)

#             if c-1: heappush(htime,(time+n+1,c-1))
#             time+=1
            
#         return time-1

        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        cnt=Counter(tasks)
        mxf=max(cnt.values())
        mxcnt=list(cnt.values()).count(mxf)
        return max(len(tasks),(n+1)*(mxf-1)+mxcnt)



        
        