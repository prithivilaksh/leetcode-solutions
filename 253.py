"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# class Solution:
#     def minMeetingRooms(self, ints: List[Interval]) -> int:

#         mp=defaultdict(int)
#         for i in ints:
#             mp[i.start]+=1
#             mp[i.end]-=1
        
#         cum,res=0,0
#         for k in sorted(mp.keys()):
#             cum+=mp[k]
#             res=max(res,cum)

#         return res


# class Solution:
#     def minMeetingRooms(self, ints: List[Interval]) -> int:

#         res,heap=0,[]
#         ints.sort(key=lambda a:a.start)

#         for i in ints:
#             while heap and heap[0]<=i.start:
#                 heapq.heappop(heap)
#             heapq.heappush(heap,i.end)
#             res=max(res,len(heap))

#         return res

class Solution:
    def minMeetingRooms(self, ints: List[Interval]) -> int:

        heap=[]
        ints.sort(key=lambda a:a.start)

        for i in ints:
            if heap and heap[0]<=i.start:
                heapq.heappop(heap)
            heapq.heappush(heap,i.end)

        return len(heap)


