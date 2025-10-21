
## MLE
# class Solution:
#     def findLadders(self, b: str, e: str, words: List[str]) -> List[List[str]]:
        
#         words=set(words)
#         if e not in words: return []
#         n=len(b)
#         g=defaultdict(list)

#         for word in words:
#             for j in range(n):
#                 pat=word[:j]+"_"+word[j+1:]
#                 g[pat].append(word)
        
#         dq,res=deque([[b]]),[]
#         while dq and not res:
#             for _ in range(len(dq)):
#                 curr=dq.popleft()
#                 u=curr[-1]
#                 if u==e: res.append(curr)
#                 if res: continue
#                 for j in range(n):
#                     pat=u[:j]+"_"+u[j+1:]
#                     for v in g[pat]:
#                         if v not in curr:
#                             dq.append(curr[:]+[v])
#         return res


## MLE
# class Solution:
#     def findLadders(self, b: str, e: str, words: List[str]) -> List[List[str]]:
        
#         words=set(words)
#         if e not in words: return []
#         n=len(b)
#         g=defaultdict(list)

#         for word in words:
#             for j in range(n):
#                 pat=word[:j]+"_"+word[j+1:]
#                 g[pat].append(word)
        
#         dq,vis,res=deque([[b]]),set([b]),[]
#         while dq and not res:
#             tmpvis=set()
#             for _ in range(len(dq)):
#                 curr=dq.popleft()
#                 u=curr[-1]
#                 if u==e: res.append(curr)
#                 if res: continue
#                 for j in range(n):
#                     pat=u[:j]+"_"+u[j+1:]
#                     for v in g[pat]:
#                         if v not in vis:
#                             dq.append(curr+[v])
#                             tmpvis.add(v)
#             vis.update(tmpvis)
#         return res


# class Solution:
#     def findLadders(self, b: str, e: str, words: List[str]) -> List[List[str]]:
        
#         words=set(words)
#         if e not in words: return []
#         n,res=len(b),[]
#         g,par=defaultdict(list),defaultdict(list)

#         for word in words:
#             for j in range(n):
#                 pat=word[:j]+"_"+word[j+1:]
#                 g[pat].append(word)
        
#         dq,vis,res=deque([b]),set([b]),[]
#         while dq:
#             tmpvis=set()
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 if u==e: break 
#                 for j in range(n):
#                     pat=u[:j]+"_"+u[j+1:]
#                     for v in g[pat]:
#                         if v not in vis:
#                             par[v].append(u)
#                             if v not in tmpvis:
#                                 dq.append(v)
#                                 tmpvis.add(v)
#             vis.update(tmpvis)
        
#         def dfs(path):
#             if path[-1]==b: res.append(path[::-1]);return
#             for v in par[path[-1]]:
#                 dfs(path+[v])
#         dfs([e])
#         return res


class Solution:
    def findLadders(self, b: str, e: str, words: List[str]) -> List[List[str]]:

        # idea/observation:
        # 1) naive approach would be to do a bfs with each distict path as an element
        # 2) highly in effecient as we solve the same problem again for eg a->b->c & x->b->c
        # 3) so instead, traverse level by level and track the visited until previous level, so that we ensure all the paths are tracked in the current level.
        # 4) finally do dfs to find all the paths.
        # 5) to build the graph in O(N), we use pattern as opposed to checking every pair O(N*N).

        words,n,res=set(words),len(b),[]
        g,par=defaultdict(set),defaultdict(set)

        if e not in words: return []

        for word in words:
            for i in range(n):
                pat=word[:i]+"_"+word[i+1:]
                g[pat].add(word)
        
        level,vis=set([b]),set([b])
        while level:
            nextlevel=set()
            for u in level:
                for i in range(n):
                    pat=u[:i]+"_"+u[i+1:]
                    for v in g[pat]:
                        if v not in vis:
                            par[v].add(u)
                            nextlevel.add(v)
            if e in nextlevel: break
            vis.update(nextlevel)
            level=nextlevel
        
        if e not in par: return []
        
        def dfs(path):
            if path[-1]==b: res.append(path[::-1]);return
            for v in par[path[-1]]: dfs(path+[v])
        dfs([e])
        return res

