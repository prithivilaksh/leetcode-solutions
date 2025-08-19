class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        n=len(arr)
        vis=[False]*n
        g=defaultdict(list)
        for i,x in enumerate(arr): g[x].append(i)
        def bfs(u):
            q=deque([u])
            vis[u]=True
            steps=0
            while q:
                for _ in range(len(q)):
                    u=q.popleft()
                    if u==n-1: return steps
                    v1,v2=u+1,u-1
                    if v1<n and not vis[v1]: vis[v1]=True;q.append(v1)
                    if v2>=0 and not vis[v2]: vis[v2]=True;q.append(v2)
                    for v3 in g[arr[u]]:
                        if not vis[v3]:
                            vis[v3]=True;q.append(v3)
                    # del g[arr[u]]
                    g[arr[u]].clear()
                steps+=1
            return -1
        return bfs(0)