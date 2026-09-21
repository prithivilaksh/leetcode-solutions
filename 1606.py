# from sortedcontainers import SortedList
# class Solution:
#     def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        
#         avlbl=SortedList([i for i in range(k)])
#         cnt,h=defaultdict(int),[]

#         for i,(s,d) in enumerate(zip(arrival,load)):

#             while h and h[0][0]<=s:
#                 server=heappop(h)[1]
#                 avlbl.add(server)
            
#             if not avlbl: continue

#             first=i%k
#             pos=bisect_left(avlbl,first)
#             if pos==len(avlbl): pos=0

#             server=avlbl[pos]
#             avlbl.remove(server)
#             heappush(h,(s+d,server))
#             cnt[server]+=1

#         mx=max(cnt.values())
#         return [k for k,v in cnt.items() if v==mx]


# from sortedcontainers import SortedList
# class Solution:
#     def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        
#         avlbl=SortedList([i for i in range(k)])
#         cnt,h=defaultdict(int),[]

#         for i,(s,d) in enumerate(zip(arrival,load)):

#             while h and h[0][0]<=s:
#                 server=heappop(h)[1]
#                 avlbl.add(server)
            
#             if not avlbl: continue

#             pos=bisect_left(avlbl,i%k)%len(avlbl)
#             server=avlbl.pop(pos)
#             heappush(h,(s+d,server))
#             cnt[server]+=1

#         mx=max(cnt.values())
#         return [k for k,v in cnt.items() if v==mx]


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        
        avlbl=[i for i in range(k)]
        cnt,h=defaultdict(int),[]

        for i,(s,d) in enumerate(zip(arrival,load)):

            while h and h[0][0]<=s:
                server=heappop(h)[1]
                heappush(avlbl,i+(server-i)%k)
            
            if not avlbl: continue

            server=heappop(avlbl)%k
            heappush(h,(s+d,server))
            cnt[server]+=1

        mx=max(cnt.values())
        return [k for k,v in cnt.items() if v==mx]



# total servers=7
# i=13
# freed server = 5

# i=9
# 2 3 4 5 6 0 1
# 4->11

# i=10
# 3 4 5 6 0 1 2
# 4->11

# i=11
# 4 5 6 0 1 2 3
# 4->11

# i=12
# 5 6 0 1 2 3 4
# 4->18

# i=13
# 6 0 1 2 3 4 5
# 4->18
