# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
        
#         par=defaultdict(lambda x:x)
#         cnt=defaultdict(lambda:1)
#         def slope(x1,y1,x2,y2):
#             dy,dx=y2-y1,x2-x1
#             return dy/dx if dx!=0 else inf
        
#         def find(x):
#             if x not in par: par[x]=x
#             if x!=par[x]:
#                 par[x]=find(par[x])
#             return par[x]
        
#         def union(a,b):
#             m=slope(*a,*b)
#             a=find((m,*a))
#             b=find((m,*b))
#             if a==b: return
#             if cnt[a]<cnt[b]: a,b=b,a
#             par[b]=a
#             cnt[a]+=cnt[b]
        
#         n=len(points)
#         for i in range(n):
#             for j in range(i+1,n):
#                 union(points[i],points[j])
        
#         return max(cnt.values(),default=1)


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        def slope(x1,y1,x2,y2):
            dy,dx=y2-y1,x2-x1
            return dy/dx if dx!=0 else inf    
        n,res=len(points),1
        for i in range(n-1):
            cnt=defaultdict(lambda:1)
            for j in range(i+1,n):
                a,b=points[i],points[j]
                cnt[slope(*a,*b)]+=1
            res=max(res,max(cnt.values()))
        return res
        


