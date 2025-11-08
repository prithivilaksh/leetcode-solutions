# ## TLE
# class Solution:
#     def largestPathValue(self, color: str, edges: List[List[int]]) -> int:
#         n,res=len(color),[-1]
#         g,cnt=defaultdict(list),defaultdict(int)
#         for u,v in edges: g[u].append(v)

#         def dfs(u):
#             cnt[color[u]]+=1
#             res[0]=max(res[0],cnt[color[u]])
#             vis.add(u)
#             for v in g[u]:
#                 if v in vis or dfs(v)==-1: return -1
#             vis.discard(u)
#             cnt[color[u]]-=1
        
#         for i in range(n):
#             vis=set()
#             if dfs(i)==-1: return -1

#         return res[0]


# class Solution:
#     def largestPathValue(self, color: str, edges: List[List[int]]) -> int:
#         n,res=len(color),-1
#         colset=set(color)
#         g,vis=defaultdict(list),defaultdict(int)
#         dp=defaultdict(lambda: defaultdict(int))

#         for u,v in edges: g[u].append(v)

#         def dfs(u):
#             if vis[u]==1: return -1
#             if vis[u]==2: return 0
#             vis[u]=1
#             for v in g[u]:
#                 if dfs(v)==-1: return -1
#                 for c in colset:
#                     dp[u][c]=max(dp[u][c],dp[v][c])
#             dp[u][color[u]]+=1
#             vis[u]=2
        
#         for i in range(n):
#             if dfs(i)==-1: return -1
#             res=max(res,dp[i][color[i]])

#         return res


class Solution:
    def largestPathValue(self, color: str, edges: List[List[int]]) -> int:


        n=len(color)
        state=[0]*n
        colorset=set(color)
        map=[defaultdict(int) for i in range(n)]
        g=defaultdict(list)

        for u,v in edges: g[u].append(v)

        def dfs(u):
            if state[u]==1: return True
            if state[u]==2: return False
            state[u]=1
            for v in g[u]:
                if dfs(v): return True
                for c in colorset:
                    map[u][c]=max(map[u][c],map[v][c])
            map[u][color[u]]+=1
            state[u]=2
            return False
        
        res=0
        for u in range(n):
            if dfs(u): return -1
            res=max(res,max(map[u].values()))
        
        return res

# class Solution:
#     def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
#         n = len(colors)
#         adj = [[] for _ in range(n)]
#         indegree = [0] * n

#         for edge in edges:
#             adj[edge[0]].append(edge[1])
#             indegree[edge[1]] += 1

#         count = [[0] * 26 for _ in range(n)]
#         q = []

#         # Push all the nodes with indegree zero in the queue.
#         for i in range(n):
#             if indegree[i] == 0:
#                 q.append(i)

#         answer = 0
#         nodesSeen = 0
#         while q:
#             node = q.pop(0)
#             answer = max(answer, count[node][ord(colors[node]) - ord('a')] + 1)
#             count[node][ord(colors[node]) - ord('a')] += 1
#             nodesSeen += 1

#             for neighbor in adj[node]:
#                 for i in range(26):
#                     # Try to update the frequency of colors for neighbor to include paths
#                     # that use node->neighbor edge.
#                     count[neighbor][i] = max(count[neighbor][i], count[node][i])

#                 indegree[neighbor] -= 1
#                 if indegree[neighbor] == 0:
#                     q.append(neighbor)

#         return -1 if nodesSeen < n else answer






















        