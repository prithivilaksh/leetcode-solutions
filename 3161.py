# # TLE 739/744
# from sortedcontainers import SortedList
# class Solution:
#     def getResults(self, qs: List[List[int]]) -> List[bool]:
        

#         arr,res=SortedList([0,inf]),[]
#         def check(l,r):
#             if l>=r: return False
#             if l+1==r: return arr[r]-arr[l]>=blk
#             if arr[r]-arr[l]<blk: return False
#             m=l+(r-l)//2
#             if check(l,m): return True
#             if check(m,r): return True
#             return False

#         for typ,*rem in qs:
#             if typ==1: arr.add(rem[0])
#             else:
#                 x,blk=rem
#                 arr.add(x)
#                 l,r=0,bisect_left(arr,x)
#                 res.append(check(l,r))
#                 arr.remove(x)
        
#         return res


## Not the most effecient | need to do again
# class Solution:
#     def getResults(self, qs: List[List[int]]) -> List[bool]:

#         coords=[q[1] for q in qs]+[0,inf]
#         c2i={c:i for i,c in enumerate(sorted(set(coords)))}

#         n=len(c2i)
#         stree,res=[0]*4*n,[]
#         sl=SortedList([0,inf])

#         def update(l,r,i,pos,val):
#             if l>r: return
#             if l==r==pos: stree[i]=val;return
#             m=l+(r-l)//2
#             if pos<=m: update(l,m,2*i+1,pos,val)
#             else: update(m+1,r,2*i+2,pos,val)
#             stree[i]=max(stree[2*i+1],stree[2*i+2])
        
#         def query(l,r,i,ql,qr):
#             if qr<l or r<ql: return 0
#             if ql<=l<=r<=qr: return stree[i]
#             m=l+(r-l)//2
#             return max(query(l,m,2*i+1,ql,qr),query(m+1,r,2*i+2,ql,qr))
            

#         update(0,n-1,0,0,inf)
#         for i,(t,x,*blk) in enumerate(qs):
#             if t==1: 
#                 l=bisect_left(sl,x)-1
#                 r=bisect_right(sl,x)
#                 l,r=sl[l],sl[r]
#                 update(0,n-1,0,c2i[l],x-l)
#                 update(0,n-1,0,c2i[x],r-x)
#                 sl.add(x)
#             else:
#                 l=bisect_right(sl,x-blk[0])-1
#                 while l>=0 and sl[l]>x-blk[0]:l-=1
#                 if l==-1: res.append(False);continue
#                 l=sl[l]
#                 ans=query(0,n-1,0,0,c2i[l])
#                 res.append(ans>=blk[0])
#         return res
        

