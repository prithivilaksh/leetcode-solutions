# import gc
# class Solution:
#     def minJumps(self, nums: List[int]) -> int:

#         x=max(nums)
#         prime=[True]*(x+1)
#         prime[0]=prime[1]=False

#         n=len(nums)
#         g=defaultdict(set)
#         ntoi=defaultdict(list)
#         for i,u in enumerate(nums): ntoi[u].append(i)

#         p=2
#         while p*p<=x:
#             if prime[p]:                  
#                 for i in range(p*p,x+1,p):
#                     prime[i]=False
#             p+=1

#         for p in nums:
#             if prime[p] and p in ntoi :
#                 for i in range(p,x+1,p):
#                     if i in ntoi:
#                         for u in ntoi[p]:
#                             for v in ntoi[i]:
#                                 if u!=v:
#                                     g[u].add(v)
                                

#         del ntoi
#         del prime
#         gc.collect()

        
#         q=[(0,0)]
#         vis=[False]*(n+1)
#         vis[0]=True

#         while q:
#             d,u=heappop(q)

#             if u==n-1 or d==n-1: return d
            
#             for v in g[u]:
#                 if not vis[v]:
#                     vis[v]=True
#                     heappush(q,(d+1,v))

#             if u+1<n and not vis[u+1]: 
#                 vis[u+1]=True
#                 heappush(q,(d+1,u+1))
#             if u-1>=0 and not vis[u-1]: 
#                 vis[u-1]=True
#                 heappush(q,(d+1,u-1))

#         return n-1


# TLE
# class Solution:
#     def minJumps(self, nums: List[int]) -> int:

#         n=max(nums)
#         prime=[True]*(n+1)
#         prime[0]=prime[1]=False
#         p=2
#         while p*p<=n:
#             if prime[p]:
#                 for i in range(p*p,n+1,p):
#                     prime[i]=False
#             p+=1

        
#         n=len(nums)
#         vis=[False]*n
#         q=deque([(0,0)])
#         vis[0]=True

#         while q:
#             u,d=q.popleft()

#             if d==n-1 or u==n-1: return d

#             if u-1>=0 and not vis[u-1]: q.append((u-1,d+1))
#             if u+1<n and not vis[u+1]: q.append((u+1,d+1))

#             if prime[nums[u]]:
#                 for v,x in enumerate(nums):
#                     if x%nums[u]==0 and not vis[v]: #u!=v covered with not vis[v]
#                         q.append((v,d+1))

#         return n-1



#TLE
# class Solution:
#     def minJumps(self, nums: List[int]) -> int:

#         st=set(nums)
#         n=max(st)
#         prime=[True]*(n+1)
#         prime[0]=prime[1]=False
#         p=2
#         while p*p<=n:
#             if prime[p]:
#                 for i in range(p*p,n+1,p):
#                     prime[i]=False
#             p+=1

        
#         g=defaultdict(list)
#         for u,x in enumerate(nums):
#             if prime[x]:
#                 for v,y in enumerate(nums):
#                     if u!=v and y%x==0:
#                         g[u].append(v)
         
#         n=len(nums)
#         vis=[False]*n
#         q=deque([(0,0)])
#         vis[0]=True

#         while q:
#             u,d=q.popleft()
#             if d==n-1 or u==n-1: return d
#             if u-1>=0 and not vis[u-1]: 
#                 vis[u-1]=True
#                 q.append((u-1,d+1))
#             if u+1<n and not vis[u+1]: 
#                 vis[u+1]=True
#                 q.append((u+1,d+1))

#             for v in g[u]:
#                 if not vis[v]: 
#                     vis[v]=True
#                     q.append((v,d+1))

#         return n-1

# TLE
# class Solution:
#     def minJumps(self, nums: List[int]) -> int:

#         n=max(nums)
#         prime=[True]*(n+1)
#         prime[0]=prime[1]=False
#         p=2
#         while p*p<=n:
#             if prime[p]:
#                 for i in range(p*p,n+1,p):
#                     prime[i]=False
#             p+=1
        
#         st=set(nums)
#         g=defaultdict(list)
#         for i,x in enumerate(nums):
#             for p in range(2,n+1):
#                 if x==1: break
#                 if prime[p] and x%p==0:
#                     g[p].append(i)
#                     while x%p==0:
#                         x//=p
                 
#         n=len(nums)
#         vis=[False]*n
#         vis[0]=True
#         q=deque([(0,0)])
#         while q:
#             u,d=q.popleft()
#             if d==n-1 or u==n-1: return d
#             if u-1>=0 and not vis[u-1]: 
#                 vis[u-1]=True;q.append((u-1,d+1))
#             if u+1<n and not vis[u+1]: 
#                 vis[u+1]=True;q.append((u+1,d+1))
#             for v in g[nums[u]]:
#                 if u !=v and not vis[v]: 
#                     vis[v]=True;q.append((v,d+1))
#             del g[nums[u]]
#         return n-1



# class Solution:
#     def minJumps(self, nums: List[int]) -> int:

#         n=max(nums)
#         g=defaultdict(list)
#         for i,x in enumerate(nums):
#             for p in range(2,n+1):
#                 if x==1: break
#                 if x%p==0:
#                     g[p].append(i)
#                     while x%p==0:
#                         x//=p               
                 
#         n=len(nums)
#         vis=[False]*n
#         vis[0]=True
#         q=deque([(0,0)])
#         while q:
#             u,d=q.popleft()
#             if d>=n-1 or u==n-1: return d
#             if u-1>=0 and not vis[u-1]: 
#                 vis[u-1]=True;q.append((u-1,d+1))
#             if u+1<n and not vis[u+1]: 
#                 vis[u+1]=True;q.append((u+1,d+1))
#             for v in g[nums[u]]:
#                 if u!=v and not vis[v]: 
#                     vis[v]=True;q.append((v,d+1))
#             del g[nums[u]]
#         return n-1




# class Solution:
#     def minJumps(self, nums: List[int]) -> int:

#         n=max(nums)
#         g=defaultdict(list)
#         for i,x in enumerate(nums):
#             p=2
#             while p*p<=x:
#                 if x%p==0:
#                     g[p].append(i)
#                     while x%p==0:
#                         x//=p  
#                 p+=1
#             if x>1: g[x].append(i)              
                 
#         n=len(nums)
#         vis=[False]*n
#         vis[0]=True
#         q=deque([(0,0)])
#         while q:
#             u,d=q.popleft()
#             if d>=n-1 or u==n-1: return d
#             if u-1>=0 and not vis[u-1]: 
#                 vis[u-1]=True;q.append((u-1,d+1))
#             if u+1<n and not vis[u+1]: 
#                 vis[u+1]=True;q.append((u+1,d+1))
#             for v in g[nums[u]]:
#                 if u!=v and not vis[v]: 
#                     vis[v]=True;q.append((v,d+1))
#             del g[nums[u]]
#         return n-1



class Solution:  
    mx=1000007
    prime=[True]*mx

    @classmethod
    def fillPrime(cls):
        cls.prime[0]=cls.prime[1]=False
        p=2
        while p*p<=cls.mx:
            if cls.prime[p]:
                for i in range(p*p,cls.mx,p):
                    cls.prime[i]=False
            p+=1

    def minJumps(self, nums: List[int]) -> int:
        
        if self.prime[0]: self.fillPrime()
        
        ntoi=defaultdict(list)
        for i,x in enumerate(nums):ntoi[x].append(i)
                 
        n,mx=len(nums),max(nums)
        vis=[True]+[False]*(n-1)
        q=deque([(0,0)])
        while q:
            u,d=q.popleft()
            if d==n-1 or u==n-1: return d
            if u-1>=0 and not vis[u-1]: 
                vis[u-1]=True;q.append((u-1,d+1))
            if u+1<n and not vis[u+1]: 
                vis[u+1]=True;q.append((u+1,d+1))
            if not self.prime[nums[u]]: continue
            
            i=1
            while nums[u]*i<=mx:
                pmul=nums[u]*i
                for v in ntoi[pmul]:
                    if not vis[v]:
                        vis[v]=True;q.append((v,d+1))
                del ntoi[pmul]
                i+=1
        return n-1