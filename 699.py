# class Solution:
#     def fallingSquares(self, poss: List[List[int]]) -> List[int]:
        

#         # idea :
#         #     for each position:
#         #         prev=get the max from [l,r)
#         #         update max from [l,r) to prev+curr

#         coords=sorted(set([l for l,_ in poss]+[l+sd-1 for l,sd in poss]))
#         mp={c:i for i,c in enumerate(coords)}
#         n=len(coords)
#         stree,lazy=[0]*4*n,[0]*4*n

#         def update(l,r,i,val,ql,qr):
#             if r<ql or qr<l: return

#             # if l==r: stree[i]=val; return

#             if lazy[i]:
#                 stree[i]=lazy[i]
#                 if l!=r: lazy[2*i+1]=lazy[2*i+2]=lazy[i]
#                 lazy[i]=0

#             if ql<=l and r<=qr:
#                 stree[i]=val
#                 if l!=r: lazy[2*i+1]=lazy[2*i+2]=val
#                 return

#             m=l+(r-l)//2
#             update(l,m,2*i+1,val,ql,qr)
#             update(m+1,r,2*i+2,val,ql,qr)
#             stree[i]=max(stree[2*i+1],stree[2*i+2])

#         def query(l,r,i,ql,qr):
#             if r<ql or qr<l: return 0

#             if lazy[i]:
#                 stree[i]=lazy[i]
#                 if l!=r: lazy[2*i+1]=lazy[2*i+2]=lazy[i]
#                 lazy[i]=0

#             if ql<=l and r<=qr: return stree[i]
#             m=l+(r-l)//2
#             return max(query(l,m,2*i+1,ql,qr),query(m+1,r,2*i+2,ql,qr))
        
#         res=[0]
#         for ql,sd in poss:
#             qr=mp[ql+sd-1]
#             ql=mp[ql]
#             prev=query(0,n-1,0,ql,qr)
#             update(0,n-1,0,prev+sd,ql,qr)
#             res.append(max(res[-1],prev+sd))
        
#         return res[1:]



# class Solution:
#     def fallingSquares(self, poss: List[List[int]]) -> List[int]:

#         coords=sorted(set([l for l,_ in poss]+[l+sd for l,sd in poss]))
#         mp={x:i for i,x in enumerate(coords)}
#         h=[0]*len(coords)
#         res=[0]
#         for l,sd in poss:
#             r=l+sd
#             l,r=mp[l],mp[r]
#             prev=max(h[l:r])
#             for i in range(l,r):
#                 h[i]=prev+sd
#             res.append(max(res[-1],prev+sd))
        
#         return res[1:]
            



class Solution:
    def fallingSquares(self, pos: List[List[int]]) -> List[int]:
        
        posset=sorted(set([l for l,_ in pos]+[l+sl for l,sl in pos]))
        mp={x:i for i,x in enumerate(posset)}
        n=len(posset)
        stree=[0]*(4*n)
        lazy=[0]*(4*n)

        def lazyupdate(l,r,i):
            if lazy[i]:
                stree[i]=lazy[i]
                if l!=r: lazy[2*i+1]=lazy[2*i+2]=lazy[i]
                lazy[i]=0

        def query(l,r,i,ql,qr):
            if qr<l or r<ql: return 0
            lazyupdate(l,r,i)
            if ql<=l<=r<=qr: return stree[i]
            m=l+(r-l)//2
            return max(query(l,m,2*i+1,ql,qr),query(m+1,r,2*i+2,ql,qr))

        def update(l,r,i,ql,qr,nv):
            if qr<l or r<ql: return 
            # if l==r: stree[i]=nv;return
            if ql<=l<=r<=qr:
                lazy[i]=nv
                lazyupdate(l,r,i)
                return
            lazyupdate(l,r,i)
            m=l+(r-l)//2
            update(l,m,2*i+1,ql,qr,nv)
            update(m+1,r,2*i+2,ql,qr,nv)
            stree[i]=max(stree[2*i+1],stree[2*i+2])

        res=[0]
        for l,sl in pos:
            r=l+sl
            ql,qr=mp[l],mp[r]-1
            h=query(0,n-1,0,ql,qr)
            update(0,n-1,0,ql,qr,h+sl)
            res.append(max(res[-1],h+sl))

        return res[1:]

# class Solution:
#     def fallingSquares(self, pos: List[List[int]]) -> List[int]:
        
#         posset=sorted(set([l for l,_ in pos]+[l+sl for l,sl in pos]))
#         mp={x:i for i,x in enumerate(posset)}
#         n=len(posset)
#         h,res=[0]*n,[0]

#         for l,sl in pos:
#             r=l+sl
#             ql,qr=mp[l],mp[r]
#             ht=max(h[ql:qr])
#             for i in range(ql,qr): h[i]=ht+sl
#             res.append(max(res[-1],ht+sl))

#         return res[1:]












