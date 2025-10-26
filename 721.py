# class UnionFind:
#     def __init__(self, n):
#         self.pars = [i for i in range(n)]

#     def find(self, x):
#         while x != self.pars[x]:
#             self.pars[x] = self.pars[self.pars[x]]
#             x = self.pars[x]
#         return x
    
#     def union(self, x1, x2):
#         p1, p2 = self.find(x1), self.find(x2)
#         if p1 == p2: return False
#         self.pars[p2] = p1
#         return True

# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         UF = UnionFind(len(accounts))
#         emailToIndex = {}

#         # find relations
#         for i in range(len(accounts)):
#             for e in accounts[i][1:]:
#                 if e in emailToIndex:
#                     UF.union(emailToIndex[e], i)
#                 else:
#                     emailToIndex[e] = i

#         # combine lists
#         mergedAccounts = defaultdict(list)
#         for email, i in emailToIndex.items():
#             leader = UF.find(i)
#             mergedAccounts[leader].append(email)

#         # format output
#         res = []
#         for i, emails in mergedAccounts.items():
#             name = accounts[i][0]
#             res.append([name] + sorted(emails))
        
#         return res





class Solution:
    def accountsMerge(self, accnts: List[List[str]]) -> List[List[str]]:
        
        par={}
        em2nm=defaultdict(str)
        em2em=defaultdict(list)
        def find(x):
            par[x]=par.get(x,x)
            if x!=par[x]:
                par[x]=find(par[x])
            return par[x]
        def union(a,b):
            a,b=find(a),find(b)
            par[b]=a
        
        for acc in accnts:
            nm,em=acc[0],acc[1]
            for oem in acc[1:]:
                em2nm[oem]=nm
                union(em,oem)
        
        for em,nm in em2nm.items():
            em2em[find(em)].append(em)
        
        res=[]
        for em,ems in em2em.items():
            res.append([em2nm[em]]+sorted(ems))
        return res

        
        