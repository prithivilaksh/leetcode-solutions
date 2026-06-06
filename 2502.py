# class Allocator:

#     def __init__(self, n: int):
#         self.blk=[0]*n

#     def allocate(self, size: int, mID: int) -> int:
#         cnt=0
#         for i,x in enumerate(self.blk):
#             cnt=cnt+1 if x==0 else 0
#             if cnt==size:
#                 self.blk[i+1-size:i+1]=[mID]*size
#                 return i+1-size
#         return -1

#     def freeMemory(self, mID: int) -> int:
#         cnt=0
#         for i,x in enumerate(self.blk):
#             if x==mID: 
#                 self.blk[i]=0
#                 cnt+=1
#         return cnt


# # Your Allocator object will be instantiated and called as such:
# # obj = Allocator(n)
# # param_1 = obj.allocate(size,mID)
# # param_2 = obj.freeMemory(mID)

class Allocator:

    def __init__(self, n: int):
        self.n=n
        self.free=[[0,n]]
        self.inuse=defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        for i,(s,l) in enumerate(self.free):
            if size<=l:
                if size==l:self.free.pop(i)
                else: self.free[i]=[s+size,l-size]
                self.inuse[mID].append([s,size])
                return s
        return -1 

    def freeMemory(self, mID: int) -> int:
        freed=0
        for s,l in self.inuse[mID]:
            freed+=l
            bisect.insort(self.free,[s,l])
        del self.inuse[mID]
        self.condense()
        return freed
    
    def condense(self):
        newfree=self.free[:1]
        for s,l in self.free[1:]:
            if newfree[-1][0]+newfree[-1][1]==s: newfree[-1][1]+=l
            else: newfree.append([s,l])
        self.free=newfree
            


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)