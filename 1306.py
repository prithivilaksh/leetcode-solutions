# class Solution:
#     def canReach(self, arr: List[int], start: int) -> bool:
        
#         n=len(arr)
#         vis=[False]*n
#         def dfs(u):
#             if arr[u]==0: return True
#             vis[u]=True
#             v1,v2=u+arr[u],u-arr[u]
#             if v1<n and not vis[v1] and dfs(v1): return True
#             if v2>=0 and not vis[v2] and dfs(v2): return True
#             return False
#         return dfs(start)

# class Solution:
#     def canReach(self, arr: List[int], start: int) -> bool:
        
#         n=len(arr)
#         vis=[False]*n
#         def bfs(u):
#             q=deque([u])
#             vis[u]=True
#             while q:
#                 u=q.popleft()
#                 if arr[u]==0: return True
#                 v1,v2=u+arr[u],u-arr[u]
#                 if v1<n and not vis[v1]: vis[v1]=True;q.append(v1)
#                 if v2>=0 and not vis[v2]: vis[v2]=True;q.append(v2)
#             return False
#         return bfs(start)



# class Solution:
#     def canReach(self, arr: List[int], start: int) -> bool:
        
#         n=len(arr)
#         def dfs(u):
#             if arr[u]==0: return True
#             v1,v2=u+arr[u],u-arr[u]
#             arr[u]=-arr[u]
#             if v1<n and arr[v1]>=0 and dfs(v1): return True
#             if v2>=0 and arr[v2]>=0 and dfs(v2): return True
#         return bool(dfs(start))

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n=len(arr)
        def bfs(u):
            q=deque([u])
            arr[u]=-arr[u]
            while q:
                u=q.popleft()
                if arr[u]==0: return True
                v1,v2=u-arr[u],u+arr[u]
                if v1<n and arr[v1]>=0: arr[v1]=-arr[v1];q.append(v1)
                if v2>=0 and arr[v2]>=0: arr[v2]=-arr[v2];q.append(v2)
        return bool(bfs(start))



