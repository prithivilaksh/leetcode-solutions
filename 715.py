class RangeModule:

    def __init__(self):
        self.arr=[]

    def _findIndex(self,x):
        arr=self.arr
        pos=bisect_right(arr,x,key=lambda a:a[0])-1
        if pos!=-1:
            l,r=arr[pos]
            if l<=x<=r: return pos,True
        return pos,False

    def _addRange(self,l,r):
        arr=self.arr
        lpos,lp=self._findIndex(l)
        rpos,rp=self._findIndex(r)

        if lp: l=arr[lpos][0]
        else: lpos+=1

        if rp: r=arr[rpos][1]
        else: rpos=rpos

        arr[lpos:rpos+1]=[[l,r]]

        if lpos-1>=0 and arr[lpos-1][1]+1==arr[lpos][0]:
            newl,newr=arr[lpos-1][0],arr[lpos][1]
            arr[lpos-1:lpos+1]=[[newl,newr]]
            lpos-=1
        
        if lpos+1<len(arr) and arr[lpos][1]+1==arr[lpos+1][0]:
            newl,newr=arr[lpos][0],arr[lpos+1][1]
            arr[lpos:lpos+2]=[[newl,newr]]

    def _queryRange(self,l,r):
        arr=self.arr
        lpos,lp=self._findIndex(l)
        rpos,rp=self._findIndex(r)
        return lp and rp and lpos==rpos

    def _removeRange(self,l,r):
        arr=self.arr
        lpos,lp=self._findIndex(l)
        rpos,rp=self._findIndex(r)
        if lpos==rpos:
            pos=lpos
            if pos==-1 or pos==len(arr) or len(arr)==0: pass
            elif r<arr[pos][0] or arr[pos][1]<l: pass
            elif l<=arr[pos][0]<=arr[pos][1]<=r: arr[pos:pos+1]=[]
            elif arr[pos][0]<l<=r<arr[pos][1]:arr[pos:pos+1]=[[arr[pos][0],l-1],[r+1,arr[pos][1]]]
            elif l<=arr[pos][0]: arr[pos:pos+1]=[[r+1,arr[pos][1]]]
            elif arr[pos][1]<=r: arr[pos:pos+1]=[[arr[pos][0],l-1]]
            
        else:
            if lp:
                if arr[lpos][0]<l:
                    arr[lpos][1]=l-1
                    lpos+=1
            else: lpos+=1

            if rp:
                if r<arr[rpos][1]:
                    arr[rpos][0]=r+1
                    rpos-=1
            else: rpos=rpos

            arr[lpos:rpos+1]=[]




    def addRange(self, l: int, r: int) -> None:
        self._addRange(l,r-1)

    def queryRange(self, l: int, r: int) -> bool:
        return self._queryRange(l,r-1)

    def removeRange(self, l: int, r: int) -> None:
        self._removeRange(l,r-1)    


# # Your RangeModule object will be instantiated and called as such:
# # obj = RangeModule()
# # obj.addRange(left,right)
# # param_2 = obj.queryRange(left,right)
# # obj.removeRange(left,right)


# class Node:
#     def __init__(self, l, r, cover=False,lnode=None, rnode=None):
#         self.cover = cover
#         self.left = lnode
#         self.right = rnode
#         self.L = l
#         self.R = r
        
# class RangeModule:
    
#     def updateRange(self, node, val, qs, qe):
#         if qe < node.L or node.R < qs:
#             return
#         if qs <= node.L and node.R <= qe:
#             node.cover = val
#             node.left = node.right = None # Imp: purge all child if the range of this node is updated.
#             return
        
#         if not node.left:
#             m = (node.L + node.R)//2
#             node.left = Node(node.L, m, node.cover)
#             node.right = Node(m+1, node.R, node.cover)

#         self.updateRange(node.left, val, qs, qe)
#         self.updateRange(node.right, val, qs, qe)
#         node.cover = node.left.cover and node.right.cover

#     def __init__(self):
#         self.T = Node(1, 1000000000)
        

#     def addRange(self, qs: int, qe: int) -> None:
#         self.updateRange(self.T, True, qs, qe-1)

#     def removeRange(self, qs: int, qe: int) -> None:
#         self.updateRange(self.T, False, qs, qe-1)
    
#     def queryRange(self, qs: int, qe: int) -> bool:
#         def query(node):
#             if qe < node.L or node.R < qs:
#                 return True
            
#             if (qs <= node.L and node.R <= qe) or not node.left: # either node contained by q or cover is same for whole node.
#                 return node.cover
            
#             return query(node.left) and query(node.right)
        
#         qe -= 1
#         return query(self.T)
