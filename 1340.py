# class Solution:
#     def maxJumps(self, arr: List[int], d: int) -> int:
        
#         n=len(arr)
#         dp=[0]*n
#         for x,i in sorted(((x,i) for i,x in enumerate(arr))):
#             l,r,mx=i-1,i+1,0
#             for l in range(i-1,i-d-1,-1):
#                 if l<0 or arr[l]>=arr[i]:break
#                 mx=max(mx,dp[l])
#             for r in range(i+1,i+d+1,1):
#                 if r>=n or arr[i]<=arr[r]:break
#                 mx=max(mx,dp[r])
#             dp[i]=mx+1
        
#         return max(dp)

# class Solution:
#     def maxJumps(self, arr: List[int], d: int) -> int:
        
#         @cache
#         def dp(i):
#             l,r,mx=i-1,i+1,0
#             for l in range(i-1,i-d-1,-1):
#                 if l<0 or arr[l]>=arr[i]:break
#                 mx=max(mx,dp(l))
#             for r in range(i+1,i+d+1,1):
#                 if r>=n or arr[i]<=arr[r]:break
#                 mx=max(mx,dp(r))
#             return mx+1

#         n,res=len(arr),0
#         for i in range(n):
#             res=max(res,dp(i))
        
#         return res

# class Solution:
#     def maxJumps(self, arr: List[int], d: int) -> int:
        
#         @cache
#         def dp(i):
#             l,r,mx=i-1,i+1,0
#             for l in range(i-1,i-d-1,-1):
#                 if l<0 or arr[l]>=arr[i]:break
#                 mx=max(mx,dp(l))
#             for r in range(i+1,i+d+1,1):
#                 if r>=n or arr[i]<=arr[r]:break
#                 mx=max(mx,dp(r))
#             return mx+1

#         n=len(arr)
        
#         return max([dp(i) for i in range(n)])


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        n=len(arr)
        g=defaultdict(list)

        st=[]
        for i in range(n):
            while st and arr[st[-1]]<arr[i] and i-st[-1]<=d:
                g[i].append(st.pop())
            st.append(i)
        
        st=[]
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]<arr[i] and st[-1]-i<=d:
                g[i].append(st.pop())
            st.append(i)
        
        @cache
        def depth(u):
            return 1+max(map(depth,g[u]),default=0)

        return max(map(depth,range(n)))
