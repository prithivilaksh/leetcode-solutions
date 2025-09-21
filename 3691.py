class Stree:
    def __init__(self,n):
        self.n=n
        self.mx=[-inf]*(2*n+1)
        self.mi=[inf]*(2*n+1)
    
    def update(self,i,val):
        i+=self.n
        self.mx[i]=self.mi[i]=val
        while i:
            i//=2
            self.mx[i]=max(self.mx[2*i],self.mx[2*i+1])
            self.mi[i]=min(self.mi[2*i],self.mi[2*i+1])

    def query(self,l,r):
        l+=self.n;r+=self.n
        mx,mi=-inf,inf
        while l<r:
            if l&1:
                mx=max(mx,self.mx[l])
                mi=min(mi,self.mi[l])
                l+=1
            if r&1:
                r-=1
                mx=max(mx,self.mx[r])
                mi=min(mi,self.mi[r])
            l//=2;r//=2
        return mi-mx

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n=len(nums)
        stree=Stree(n)
        h,res=[],0
        for i,x in enumerate(nums):
            stree.update(i,x)
            heappush(h,(stree.query(0,i+1),0,i))
        
        for _ in range(k):
            diff,i,j=heappop(h)
            res+=-diff;k-=1
            if i+1<=j: heappush(h,(stree.query(i+1,j+1),i+1,j))
        return res