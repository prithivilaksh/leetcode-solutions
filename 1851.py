

# class Solution:

#     def minInterval(self, ivals: List[List[int]], qs: List[int]) -> List[int]:

#         points=set()
#         for x,y in ivals: points.add(x);points.add(y)
#         for q in qs: points.add(q)
#         points=sorted(points)
#         comp={x:i for i,x in enumerate(points)}

#         n=len(comp)
#         stree,lazy=[inf]*4*n,[inf]*4*n
#         def propagate(l,r,i):
#             if lazy[i]!=inf:
#                 stree[i]=min(stree[i],lazy[i])
#                 if l!=r:
#                     lazy[2*i+1]=min(lazy[2*i+1],lazy[i])
#                     lazy[2*i+2]=min(lazy[2*i+2],lazy[i])
#                 lazy[i]=inf

#         def update(l,r,i,ql,qr,val):
#             if r<ql or qr<l: return
#             propagate(l,r,i)
#             if ql<=l and r<=qr:
#                 lazy[i]=val
#                 propagate(l,r,i)
#                 return
                
#             m=l+(r-l)//2
#             update(l,m,2*i+1,ql,qr,val)
#             update(m+1,r,2*i+2,ql,qr,val)
#             stree[i]=min(stree[2*i+1],stree[2*i+2])


#         def query(l,r,i,pos):
#             propagate(l,r,i)
#             if l==r==pos: return stree[i]
#             m=l+(r-l)//2
#             if pos<=m: return query(l,m,2*i+1,pos)
#             return query(m+1,r,2*i+2,pos)


#         for x,y in ivals:
#             l=y-x+1
#             x,y=comp[x],comp[y]
#             update(0,n-1,0,x,y,l)

#         for i,q in enumerate(qs):
#             q=comp[q]
#             ires=query(0,n-1,0,q)
#             qs[i]=ires if ires!=inf else -1
        
#         return qs


class Solution:
    def minInterval(self, ivals: List[List[int]], qs: List[int]) -> List[int]:

        n=len(ivals)
        ivals.sort()

        h,i,res=[],0,defaultdict(lambda:-1)
        size = lambda x: x[1]-x[0]+1
        for q in sorted(qs):
            while i<n and ivals[i][0]<=q:
                heappush(h,(size(ivals[i]),ivals[i][1]))
                i+=1
            
            while h and h[0][1]<q: heappop(h)

            if h: res[q]=h[0][0]
        
        return [res[q] for q in qs]


        