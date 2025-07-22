# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.n=len(nums)
#         self.stree=[0]*4*self.n

#         def build(l,r,i):
#             if l==r: self.stree[i]=nums[l];return
#             m=l+(r-l)//2
#             build(l,m,2*i+1)
#             build(m+1,r,2*i+2)
#             self.stree[i]=self.stree[2*i+1]+self.stree[2*i+2]
#         build(0,self.n-1,0)

#     def update(self, index: int, val: int) -> None:

#         def update(l,r,i,pos,val):
#             if l==r: self.stree[i]=val; return
#             m=l+(r-l)//2
#             if pos<=m: update(l,m,2*i+1,pos,val)
#             else: update(m+1,r,2*i+2,pos,val)
#             self.stree[i]=self.stree[2*i+1]+self.stree[2*i+2]
#         update(0,self.n-1,0,index,val)
        

#     def sumRange(self, left: int, right: int) -> int:

#         def sum(l,r,i,ql,qr):
#             if ql<=l and r<=qr: return self.stree[i]
#             if qr<l or r<ql: return 0
#             m=l+(r-l)//2
#             return sum(l,m,2*i+1,ql,qr)+sum(m+1,r,2*i+2,ql,qr)
        
#         return sum(0,self.n-1,0,left,right)
        


# # Your NumArray object will be instantiated and called as such:
# # obj = NumArray(nums)
# # obj.update(index,val)
# # param_2 = obj.sumRange(left,right)


class NumArray:

    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.stree=[0]*2*self.n
        for i in range(self.n):
            self.stree[i+self.n]=nums[i]
        
        for i in range(self.n-1,0,-1):
            self.stree[i]=self.stree[2*i]+self.stree[2*i+1]        

    def update(self, i: int, val: int) -> None:
        i += self.n
        self.stree[i] = val
        while i > 1:
            i//=2
            self.stree[i] = self.stree[2*i] + self.stree[2*i+1]
        

    def sumRange(self, l: int, r: int) -> int:
        l+=self.n
        r+=self.n+1
        s=0
        while l<r:
            if l&1:
                s+=self.stree[l]
                l+=1
            if r&1:
                r-=1
                s+=self.stree[r]
            l//=2
            r//=2
        return s


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums=nums
#         self.n=len(nums)+1
#         self.f=[0]*self.n  

#         for i,x in enumerate(nums):
#             i+=1
#             self.f[i]+=x
#             p=i+(i&-i)
#             if p<self.n: self.f[p]+=self.f[i]
        

#     def update(self, i: int, val: int) -> None:
#         delta=val-self.nums[i]
#         self.nums[i]=val
#         i+=1
#         while i<self.n:
#             self.f[i]+=delta
#             i+=i&-i
        

#     def sumRange(self, left: int, right: int) -> int:
#         def sumTill(i):
#             i+=1
#             s=0
#             while i>0:
#                 s+=self.f[i]
#                 i-=i&-i
#             return s
#         return sumTill(right)-sumTill(left-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)