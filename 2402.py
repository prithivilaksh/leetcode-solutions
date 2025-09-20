# class Solution:
#     def mostBooked(self, n: int, meets: List[List[int]]) -> int:
        
#         meets.sort(key=lambda x:x[0])
#         cnt,mx=[0]*n,0
#         a,h=[i for i in range(n)],[]

#         for s,e in meets:
#             while h and h[0][0]<=s:
#                 _,room=heappop(h)
#                 heappush(a,room)
#             if not a:
#                 ne,room=heappop(h)
#                 s,e=ne,ne+e-s
#                 heappush(a,room)

#             room=heappop(a)
#             cnt[room]+=1
#             heappush(h,(e,room))
        
#         for i in range(n):
#             if cnt[i]>cnt[mx]:mx=i
#         return mx

class Solution:
    def mostBooked(self, n: int, meets: List[List[int]]) -> int:
        
        meets.sort(key=lambda x:x[0])
        cnt,mx=[0]*n,0
        a,h=[i for i in range(n)],[]

        for s,e in meets:
            while h and h[0][0]<=s:
                _,room=heappop(h)
                heappush(a,room)
            if a: room=heappop(a)
            else:
                ne,room=heappop(h)
                s,e=ne,ne+e-s
            heappush(h,(e,room))
            cnt[room]+=1

        for i in range(n):
            if cnt[i]>cnt[mx]:mx=i
        return mx

