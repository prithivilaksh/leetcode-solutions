class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1: return 0
        p=[True]*n
        p[0]=p[1]=False

        i=2
        while i*i<n:
            if p[i]:
                for j in range(i*i,n,i):
                    p[j]=False
            i+=1

        return sum(p)