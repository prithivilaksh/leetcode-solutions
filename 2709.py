# class Solution:

#     @cache
#     @staticmethod
#     def getFactors(x): 
#         i,f=2,set([x])
#         while i*i<=x:
#             if x%i==0: 
#                 f.add(i)
#                 f.add(x//i)
#             i+=1
#         return f

#     # @cache
#     # @staticmethod
#     # def getPrimes(mx):
#     #     primes=[True]*(mx+1)
#     #     primes[0]=primes[1]=False
#     #     i=2
#     #     while i*i<=mx:
#     #         if prime[i]:
#     #             for p in range(i*i,mx+1,i)
#     #                 primes[p]=False
#     #         i+=1
#     #     return [i for i in primes if i==True]

#     # @cache
#     # @staticmethod
#     # def getPrimeFactors(x): 
#     #     i,f=2,set([x])
#     #     for i in primes:
#     #         if i>x:break
#     #         if x%i==0: f.add(i)
#     #     return f

#     def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
#         # idea
#         # - if nums[0] can traverse to all j from 1-n, then nums[j] can go to nums[0] and in turn to all others
#         # - find factors for every number and union them
#         # - after unioning if there is one root then True else False

#         if len(nums)==1: return True
#         nums=set(nums)
#         if 1 in nums: return False


#         par=defaultdict(lambda:-1)
#         def find(x):
#             if x!=par[x]:
#                 par[x]=find(par[x])
#             return par[x]
        
#         def union(a,b):
#             a,b=find(a),find(b)
#             par[a]=b
        

#         for x in nums:
#             factors=Solution.getFactors(x).copy()
#             a=factors.pop()
#             if a not in par: par[a]=a
#             for b in factors: 
#                 if b not in par: par[b]=b
#                 union(a,b)
        
#         return sum(c==p for c,p in par.items())==1


class Solution:

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        # idea
        # - if nums[0] can traverse to all j from 1-n, then nums[j] can go to nums[0] and in turn to all others
        # - find factors for every number and union them
        # - after unioning if there is one root then True else False

        if len(nums)==1: return True
        nums=set(nums)
        if 1 in nums: return False
        n=len(nums)

        nums=sorted(nums)
        for i in range(n-1,0,-1):
            for j in range(i):
                if math.gcd(nums[i],nums[j])>1:
                    nums[j]*=nums[i]
                    break
            else: return False
        return True