# class Solution(object):
#     def findRedundantDirectedConnection(self, edges):
#         """
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """
#         n=len(edges)        
#         child=defaultdict(list)
#         parent=defaultdict(list)
#         def cycle(start, end):
#             if start==end: return True
#             seen.add(start)
#             for node in child[start]:
#                 if node not in seen:
#                     if cycle(node, end):
#                         return True
#             return False
        
#         K=-1          #to mark the node with 2 parents
#         for i, j in edges:      
#             child[i].append(j)
#             parent[j].append(i)
#             if len(parent[j])==2: K=j

#         if K!=-1:          # if 2-parent case happened
#             seen=set()
#             if cycle(K, parent[K][0]): return [parent[K][0], K] 
#             else:return [parent[K][1], K]
                       
#         for i in range(n-1, -1, -1):     #to find the last edge in the cycle
#             v, u=edges[i]
#             seen=set()
#             if cycle(u, v): return [v, u]


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        

        # idea/observation:
        #     - for rooted tree - root indeg=0, others indeg=1
        #     - for rooted tree + 1 edge - root indeg=0/1 , others indeg=1/2
        #     - if the extra edge connects the children
        #             There will be a cycle if a node is connected to its ancestor
        #             otherwise find node with indeg=2 
        #     - if the extra edge connects root & child, there will be a cycle, return last edge

        n=len(edges)
        par=[x for x in range(n+1)]
        def find(x):
            if x!=par[x]:
                par[x]=find(par[x])
            return par[x]
        def union(a,b):
            a,b=find(a),find(b)
            par[b]=a
            return a==b
        
        e1,e2=[],[]
        inedge=defaultdict(list)
        for u,v in edges:
            if inedge[v]:
                e1=inedge[v]
                e2=[u,v]
                break
            inedge[v]=[u,v]
        
        for u,v in edges:
            # if [u,v]==e2: continue
            if union(u,v):
                if e1: return e1 #cycle and cycle due to e1
                return [u,v] #cycle and cycle due to [u,v]
        return e2 #no cycles or cycles due to e2