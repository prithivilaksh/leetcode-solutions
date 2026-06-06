# class Solution:
#     def findMinimumTime(self, tasks: List[List[int]]) -> int:
        
#         # idea/obs:
#         # 1) we can split task in the given range
#         # 2) maximize number of tasks in the same sub range, minimizing total on time
#         # 3) total disticnt ts [1,2000]

#         tasks.sort(key=lambda x:(x[1],x[0]))
#         line=[0]*2001
#         for s,e,d in tasks:
#             for i in range(s,e+1):
#                 if line[i]: 
#                     d-=1
#                     if d==0:break
#             while d:
#                 if line[i]==0: line[i]=1;d-=1
#                 i-=1
#         return sum(line)

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        
        line=[0]*2001
        for s,e,d in sorted(tasks,key=lambda x:x[1]):
            d-=sum(line[s:e+1])
            while d>0:
                if line[e]==0: line[e]=1;d-=1
                e-=1
        return sum(line)
















