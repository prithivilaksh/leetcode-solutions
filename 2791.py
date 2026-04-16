# class Solution:
#     def countPalindromePaths(self, parent: List[int], s: str) -> int:
        
#         chi=defaultdict(list)
#         for i,x in enumerate(parent): chi[x].append(i)
        
#         res=[0]
#         cnt=defaultdict(int)
#         def dfs(u,mask):
#             cnum=ord(s[u])-ord('a')
#             cbit=1<<cnum
#             mask=mask^cbit
            
#             res[0]+=cnt[mask]
#             for i in range(26):
#                 cbit=1<<i
#                 candmask=mask^cbit
#                 res[0]+=cnt[candmask]

#             cnt[mask]+=1
#             for v in chi[u]: dfs(v,mask)

#         dfs(0,0)
#         return res[0]

# class Solution:
#     def countPalindromePaths(self, par: List[int], s: str) -> int:
        
#         @cache
#         def getmask(i):
#             if i==0: return 0
#             parmask=getmask(par[i])
#             cbit=ord(s[i])-ord('a')
#             cbin=1<<cbit
#             return parmask^cbin
        
#         cnt,res=defaultdict(int),0
#         for i in range(len(par)):
#             mask=getmask(i)
#             res+=cnt[mask]
#             for i in range(26):
#                 cbin=1<<i
#                 res+=cnt[mask^cbin]
#             cnt[mask]+=1
#         return res


class Solution:
    def countPalindromePaths(self, parent: list[int], s: str) -> int:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        count_map = defaultdict(int)
        stack = [(0, 0)]
        
        while stack:
            u, m = stack.pop()
            count_map[m]+=1
            for v in adj[u]:
                char_bit = 1 << (ord(s[v]) - ord('a'))
                stack.append((v, m ^ char_bit))
        
        total_pairs = 0
        
        for mask, freq in count_map.items():
            total_pairs += freq * (freq - 1)
            for i in range(26):
                target = mask ^ (1 << i)
                if target in count_map:
                    total_pairs += freq * count_map[target]
        
        return total_pairs//2