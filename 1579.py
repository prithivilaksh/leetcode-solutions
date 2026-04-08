# class Solution:
#     def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
#         def find(x,par):
#             if x!=par[x]:
#                 par[x]=find(par[x],par)
#             return par[x]
        
#         def union(a,b,par):
#             a,b=find(a,par),find(b,par)
#             if a==b: return False
#             par[b]=a
#             return True
        
#         apar,bpar,res=[i for i in range(n+1)],[i for i in range(n+1)],0
#         edges.sort(key=lambda x:x[0],reverse=True)
#         for t,g in groupby(edges,lambda x:x[0]):
#             for _,a,b in g:
#                 if t==3:
#                     if union(a,b,apar) and union(a,b,bpar): res+=1
#                 elif t==1:
#                     if union(a,b,apar): res+=1
#                 else:
#                     if union(a,b,bpar): res+=1

#         for par in (apar,bpar):
#             if any(find(par[1],par)!=find(par[i],par) for i in range(1,n+1)): 
#                 return -1

#         return len(edges)-res

            
# class Solution:
#     def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
#         def find(x,par):
#             if x!=par[x]:
#                 par[x]=find(par[x],par)
#             return par[x]
        
#         def union(a,b,par):
#             a,b=find(a,par),find(b,par)
#             if a==b: return False
#             par[0]+=1
#             par[b]=a
#             return True
        
#         apar,bpar,res=[i for i in range(n+1)],[i for i in range(n+1)],0
#         edges.sort(key=lambda x:x[0],reverse=True)
#         for t,g in groupby(edges,lambda x:x[0]):
#             for _,a,b in g:
#                 if t==3:
#                     if union(a,b,apar) and union(a,b,bpar): res+=1
#                 elif t==1:
#                     if union(a,b,apar): res+=1
#                 else:
#                     if union(a,b,bpar): res+=1

#         if apar[0]!=n-1 or bpar[0]!=n-1: return -1

#         return len(edges)-res


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        def find(x,par):
            if x!=par[x]:
                par[x]=find(par[x],par)
            return par[x]
        
        def union(a,b,par):
            a,b=find(a,par),find(b,par)
            if a==b: return False
            par[0]+=1 # leveraging par[0] for MST edge count
            par[b]=a
            return True
        
        alice,bob,com=[],[],[]
        apar,res=[i for i in range(n+1)],0
        for t,a,b in edges:
            if t==1: alice.append((a,b))
            elif t==2: bob.append((a,b))
            else: com.append((a,b))

        for a,b in com:
            if union(a,b,apar): res+=1
        bpar=apar[:]
        for a,b in alice:
            if union(a,b,apar): res+=1     
        for a,b in bob:
            if union(a,b,bpar): res+=1

        if apar[0]!=n-1 or bpar[0]!=n-1: return -1

        return len(edges)-res

            
