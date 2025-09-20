# class Solution:
#     def maxEvents(self, events: List[List[int]]) -> int:
        
#         events.sort(key=lambda x:x[0])
#         i=d=res=0
#         n,h=len(events),[]
#         while i<n or h:
#             if not h: d=events[i][0]
#             while h and h[0]<d:heappop(h)
#             while i<n and events[i][0]<=d:heappush(h,events[i][1]);i+=1
#             if h: res+=1;d+=1;heappop(h)
#         return res

            
# class Solution:
#     def maxEvents(self, events: List[List[int]]) -> int:
        
#         events.sort(key=lambda x:x[0])
#         mx=max(e for _,e in events)
#         i,n,h,res=0,len(events),[],0
#         for d in range(1,mx+1):
#             while h and h[0]<d:heappop(h)
#             while i<n and events[i][0]==d:heappush(h,events[i][1]);i+=1
#             if h: res+=1;heappop(h)
#         return res

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        events.sort(key=lambda x:x[1])
        mx=max(e for _,e in events)
        p=[i for i in range(mx+2)]

        def find(i):
            if i!=p[i]:
                p[i]=find(p[i])
            return p[i]
        res=0
        for s,e in events:
            d=find(s)
            if d<=e:
                res+=1
                p[d]=d+1
        return res

# class Solution:
#     def maxEvents(self, events: List[List[int]]) -> int:
        
#         events.sort(key=lambda x:x[1])
#         mx=max(e for _,e in events)
#         p=[0 for i in range(mx+2)]

#         def find(i):
#             if p[i]==0: return i
#             p[i]=find(p[i])
#             return p[i]
#         res=0
#         for s,e in events:
#             d=find(s)
#             if d<=e:
#                 res+=1
#                 p[d]=d+1
#         return res













            
