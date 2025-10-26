# class Node:
#     def __init__(self,cnt=0,lazy=0):
#         self.cnt,self.lazy=cnt,lazy
#         self.left=self.right=None

# class Stree:
#     def __init__(self):
#         self.root=Node()
    
#     def update(self,node,l,r,ql,qr):

#         if not (node.left or node.right):
#             node.left=Node()
#             node.right=Node()
        
#         if node.lazy:
#             node.cnt=r-l+1
#             node.lazy=0
#             if l!=r:
#                 node.left.lazy=node.right.lazy=1
#             return

#         if r<ql or qr<l: return

#         if ql<=l and r<=qr: 
#             node.cnt=r-l+1
#             node.lazy=0
#             if l!=r:
#                 node.left.lazy=node.right.lazy=1
#             return

#         m=l+(r-l)//2
#         self.update(node.left,l,m,ql,qr)
#         self.update(node.right,m+1,r,ql,qr)
#         node.cnt=node.left.cnt+node.right.cnt


# class CountIntervals:

#     def __init__(self):
#         self.stree=Stree()
        

#     def add(self, s: int, e: int) -> None:
#         self.stree.update(self.stree.root,0,10**9,s,e)


#     def count(self) -> int: return self.stree.root.cnt
        


# # Your CountIntervals object will be instantiated and called as such:
# # obj = CountIntervals()
# # obj.add(left,right)
# # param_2 = obj.count()


# class CountIntervals:

#         # [1,10] [20,30] [40,50] [60,70]

#         # insert [33, 37] -> [1,10] [20,30] [33,37] [40,50] [60,70]
#         # [2:2] = [33,37]

#         # insert [40,55] -> [1,10] [20,30] [40,55] [60,70]
#         # [2:3] = [40,55]

#         # insert [30,37] -> [1,10] [20,37] [40,50] [60,70]
#         # [1:2] = [20,37]

#         # insert [30,40] -> [1,10] [20,50] [60,70]
#         # [1:3] = [20,50]

#         # insert [15,55] -> [1,10] [15,55] [60,70]
#         # [1:3] = [15,55]

#     def __init__(self):
#         self.intv=[]
#         self.cnt=0
        

#     def add(self, s: int, e: int) -> None:
#         intv=self.intv

#         lpos=bisect_left(intv,s,key=lambda x:x[1])
#         rpos=bisect_right(intv,e,key=lambda x:x[0])

#         if lpos<len(intv): s=min(s,intv[lpos][0])
#         if rpos>0: e=max(e,intv[rpos-1][1])

#         todel=0
#         for i in range(lpos,rpos):
#             todel+=intv[i][1]-intv[i][0]+1
        
#         self.cnt+=e-s+1-todel
#         intv[lpos:rpos]=[[s,e]]

#     def count(self) -> int: return self.cnt
        


# # Your CountIntervals object will be instantiated and called as such:
# # obj = CountIntervals()
# # obj.add(left,right)
# # param_2 = obj.count()

class CountIntervals:

    def __init__(self):
        self.intv = []
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        intv=self.intv
        i = bisect_left(intv, left,key=lambda x: x[0])

        if i > 0 and intv[i-1][1] >= left: i -= 1

        while i < len(intv) and intv[i][0] <= right+1:
            l, r = intv[i][0], intv[i][1]
            left = min(left, l)
            right = max(right, r)
            self.cnt -= (r - l + 1)
            intv.pop(i)
        self.intv.insert(i, (left, right))
        self.cnt += (right - left + 1)

    def count(self) -> int: return self.cnt        


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()