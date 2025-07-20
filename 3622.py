class Solution:
    def checkDivisibility(self, n: int) -> bool:

        x,s,p=n,0,1
        while x:
            r=x%10
            s+=r
            p*=r
            x=x//10

        return n%(s+p)==0