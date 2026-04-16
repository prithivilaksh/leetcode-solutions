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

# class Solution:
#     def mostBooked(self, n: int, meets: List[List[int]]) -> int:
        
#         meets.sort(key=lambda x:x[0])
#         cnt,mx=[0]*n,0
#         a,h=[i for i in range(n)],[]

#         for s,e in meets:
#             while h and h[0][0]<=s:
#                 _,room=heappop(h)
#                 heappush(a,room)
#             if a: room=heappop(a)
#             else:
#                 ne,room=heappop(h)
#                 s,e=ne,ne+e-s
#             heappush(h,(e,room))
#             cnt[room]+=1

#         for i in range(n):
#             if cnt[i]>cnt[mx]:mx=i
#         return mx


# class Solution:
#     def mostBooked(self, n: int, meets: List[List[int]]) -> int:
        
#         avl,h=[i for i in range(n)],[]
#         cnt=[0]*n
#         meets.sort(key=lambda x:x[0])

#         for m in meets:
#             while h and h[0][0]<=m[0]:
#                 heappush(avl,heappop(h)[1])
#             if avl: room=heappop(avl)
#             else: 
#                 pend,room=heappop(h)
#                 m=[pend,pend+m[1]-m[0]]
            
#             heappush(h,(m[1],room))
#             cnt[room]+=1
#         mx=0
#         for i in range(n):
#             if cnt[i]>cnt[mx]:mx=i
#         return mx

class Solution:
    def mostBooked(self, n: int, meets: List[List[int]]) -> int:
        
        meets.sort(key=lambda x:x[0])
        rooms,inuse=list(range(n)),[]
        cnt=defaultdict(int)

        for s,e in meets:
            while inuse and inuse[0][0]<=s:
                _,r=heappop(inuse)
                heappush(rooms,r)
            
            if rooms:
                r=heappop(rooms)
                heappush(inuse,(e,r))
            else:
                lastend,r=heappop(inuse)
                heappush(inuse,(lastend+e-s,r))
            
            cnt[r]+=1
        
        return max(cnt, key=lambda x:cnt[x])
            













