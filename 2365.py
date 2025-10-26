# class Solution:
#     def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        
#         day=defaultdict(lambda : -100004)

#         days=1
#         for i,x in enumerate(tasks):
#             last=day[x]
#             days=max(days,last+space+1)
#             day[x]=days
#             days+=1

#         return days-1

# class Solution:
#     def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        
#         day,days=defaultdict(lambda : -100004),1

#         for x in tasks:
#             last=day[x]
#             if days<last+space+1: days=last+space+1
#             day[x]=days
#             days+=1

#         return days-1

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        
        day,days=defaultdict(int),1

        for x in tasks:
            if day[x]>days: days=day[x]
            day[x]=days+space+1
            days+=1

        return days-1