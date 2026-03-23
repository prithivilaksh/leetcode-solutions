# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
        
#         m,n=len(ring),len(key)
#         dq,vis=deque([(0,0,0)]),set()

#         while True:
#             i,j,d=dq.popleft()
#             if ring[i]==key[j]:
#                 d+=1
#                 if j==n-1: return d
#                 if (i,j+1) not in vis:
#                     vis.add((i,j+1))
#                     dq.append((i,j+1,d))
#             else:
#                 for x in (i+1,i-1):
#                     x%=m
#                     if (x,j) not in vis:
#                         vis.add((x,j))
#                         dq.append((x,j,d+1))

# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
        
#         m,n,d=len(ring),len(key),0
#         dq,vis=deque([(0,0)]),set()

#         while True:
#             for _ in range(len(dq)):
#                 i,j=dq.popleft()
#                 if ring[i]==key[j]:
#                     if j==n-1: return d+1
#                     if (i,j+1) not in vis:
#                         vis.add((i,j+1))
#                         dq.append((i,j+1))
#                 else:
#                     for x in (i+1,i-1):
#                         x%=m
#                         if (x,j) not in vis:
#                             vis.add((x,j))
#                             dq.append((x,j))
#             d+=1



# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
        
#         m,n=len(ring),len(key)

#         @cache
#         def dp(i,j):
#             if j==n: return 0

#             if ring[i]==key[j]: return 1+dp(i,j+1)

#             res=inf
            
#             d=0
#             for x in range(i+1,i+m):
#                 x%=m;d+=1
#                 if ring[x]==key[j]:
#                     res=min(res,d+1+dp(x,j+1))
#                     break

#             d=0
#             for x in range(i-1,i-m,-1):
#                 x%=m;d+=1
#                 if ring[x]==key[j]:
#                     res=min(res,d+1+dp(x,j+1))
#                     break
                    
#             return res
        
#         return dp(0,0)


# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
        
#         m,n=len(ring),len(key)
#         ind=defaultdict(list)
#         for i,c in enumerate(ring): ind[c].append(i)

#         @cache
#         def dp(i,j):
#             if j==n: return 0

#             if ring[i]==key[j]: return 1+dp(i,j+1)

            
#             indlist=ind[key[j]]
#             ln=len(indlist)
#             pos=bisect_left(indlist,i)
#             if pos==0: 
#                 lind=indlist[-1]
#                 ld=i+(m-1-lind+1)
#             else:
#                 lind=indlist[pos-1]
#                 ld=i-lind
            
#             if pos==ln:
#                 rind=indlist[0]
#                 rd=rind+(m-1-i+1)
#             else:
#                 rind=indlist[pos]
#                 rd=rind-i
                
#             return min(ld+dp(lind,j),rd+dp(rind,j))

        
#         return dp(0,0)


# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
        
#         m,n=len(ring),len(key)
#         ind=defaultdict(list)
#         for i,c in enumerate(ring): ind[c].append(i)

#         @cache
#         def dp(i,j):
#             if j==n: return 0

#             if ring[i]==key[j]: return 1+dp(i,j+1)

#             indlist=ind[key[j]]
#             ln=len(indlist)
#             pos=bisect_left(indlist,i)

#             lind=indlist[(pos-1)%ln]
#             ld=(i-lind)%m
            
#             rind=indlist[pos%ln]
#             rd=(rind-i)%m
                
#             return min(ld+dp(lind,j),rd+dp(rind,j))

        
#         return dp(0,0)


# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
        
#         m,n=len(ring),len(key)
#         ind=defaultdict(list)
#         for i,c in enumerate(ring): ind[c].append(i)

#         @cache
#         def dp(i,j):
#             if j==n: return 0

#             if ring[i]==key[j]: return 1+dp(i,j+1)

#             indlist=ind[key[j]]
#             ln=len(indlist)
#             pos=bisect_left(indlist,i)

#             lind=indlist[(pos-1)%ln]
#             ld=(i-lind)%m
            
#             rind=indlist[pos%ln]
#             rd=(rind-i)%m
                
#             return 1+min(ld+dp(lind,j+1),rd+dp(rind,j+1))

        
#         return dp(0,0)

# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
#         m,n = len(ring),len(key)
#         ind=defaultdict(list)
#         for i,c in enumerate(ring): ind[c].append(i)
    

#         h,vis = [(0, 0, 0)],set()    
#         while True:
#             d,i,j = heappop(h)
#             if j == n: return d+n
#             if (i, j) in vis: continue

#             vis.add((i, j))

#             indlist=ind[key[j]]
#             ln=len(indlist)
#             pos=bisect_left(indlist,i)

#             lind=indlist[(pos-1)%ln]
#             ld=(i-lind)%m
            
#             rind=indlist[pos%ln]
#             rd=(rind-i)%m

#             heappush(h,(d+ld,lind,j+1))
#             heappush(h,(d+rd,rind,j+1))


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m,n = len(ring),len(key)
        ind=defaultdict(list)
        for i,c in enumerate(ring): ind[c].append(i)
    
        h,vis = [(0, 0, 0)],set()    
        while True:
            d,i,j = heappop(h)
            if j == n: return d+n
            if (i,j) in vis: continue
            vis.add((i,j))

            indlist=ind[key[j]]
            ln=len(indlist)
            pos=bisect_left(indlist,i)

            lind=indlist[(pos-1)%ln]
            ld=(i-lind)%m
            rind=indlist[pos%ln]
            rd=(rind-i)%m

            if (lind,j+1) not in vis: heappush(h,(d+ld,lind,j+1))
            if (rind,j+1) not in vis: heappush(h,(d+rd,rind,j+1))