# class Solution:
#     def numSimilarGroups(self, strs: list[str]) -> int:
        
#         n,m=len(strs),len(strs[0])
#         par=[i for i in range(n)]

#         def find(x):
#             if x!=par[x]:
#                 par[x]=find(par[x])
#             return par[x]
        
#         def union(a,b):
#             a,b=find(a),find(b)
#             par[a]=b
        
#         def similar(a,b):
#             cnt=0
#             for i in range(m):
#                 if a[i]!=b[i]: 
#                     cnt+=1
#                     if cnt>2: return False
#             return True


#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if similar(strs[i],strs[j]):
#                     union(i,j)
        
#         return sum(i==par[i] for i in range(n))

class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        
        n,m=len(strs),len(strs[0])
        par=[i for i in range(n)]

        def find(x):
            if x!=par[x]:
                par[x]=find(par[x])
            return par[x]
        
        def union(a,b):
            a,b=find(a),find(b)
            par[b]=a
            return a!=b
        
        def similar(a,b):
            cnt=0
            for i in range(m):
                if a[i]!=b[i]: 
                    cnt+=1
                    if cnt>2: return False
            return True

        res=n
        for i in range(n-1):
            for j in range(i+1,n):
                if similar(strs[i],strs[j]) and union(i,j): res-=1
        
        return res

        
# class Solution:
#     def numSimilarGroups(self, strs: list[str]) -> int:
        
#         n,m=len(strs),len(strs[0])
#         par=[i for i in range(n)]
        
#         def find(x):
#             if x!=par[x]:
#                 par[x]=find(par[x])
#             return par[x]
        
#         def union(a,b):
#             a,b=find(a),find(b)
#             par[a]=b
        
#         def similar(a,b):
#             return sum(x!=y for x,y in zip(a,b))<=2

#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if similar(strs[i],strs[j]):
#                     union(i,j)
        
#         return sum(i==par[i] for i in range(n))

        
