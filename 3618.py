class Solution:
    def splitArray(self, nums: List[int]) -> int:

        def findPrimeRange(n):
            p,prime=2,[True]*(n+1)
            for i in range(min(2,n)):prime[i]=False
            while p*p<=n:
                if (prime[p] == True):
                    for i in range(p * p,n+1, p):
                        prime[i] = False
                p+=1
            return prime

        n=len(nums)
        prime=findPrimeRange(n)
        a,b=0,0
        for i,x in enumerate(nums):
            if prime[i]:a+=x
            else:b+=x

        return abs(a-b)