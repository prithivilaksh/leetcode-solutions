# class Solution:
#     def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:

#         def isPossible(cnums,k):
#             sums={0}
#             for x in cnums:
#                 st=sums.copy()
#                 for s in st: 
#                     if s+x==k: return True
#                     sums.add(s+x)
#             return False
            
#         n=len(nums)
#         res=[]
#         for x in range(1,n+1):
#             cnums=[min(a,x) for a in nums]
#             res.append(isPossible(cnums,k))
#         return res

# class Solution:
#     def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:

#         def isPossible(cnums):
#             sums=0
#             for x in cnums:
#                 sums= sums | sums<<x | 1<<x
#             return sums>>k & 1 == 1
            
#         n=len(nums)
#         res=[]
#         for x in range(1,n+1):
#             cnums=[min(a,x) for a in nums]
#             res.append(isPossible(cnums))
#         return res

# class Solution:
#     def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
            
#         n=len(nums)
#         res=[]
#         for x in range(1,n+1):
#             sums=1
#             for a in nums:
#                 c=min(x,a)
#                 sums|=sums<<c
#             res.append(sums>>k & 1 == 1)
#         return res


# class Solution:
#     def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
#         nums.sort()
#         n=len(nums)
#         res=[]
#         sums=1
#         mask=(1<<(k+1)) -1
#         it=0
#         for x in range(1,n+1):
#             while it<n and nums[it]<=x:
#                 sums|=sums<<x & mask
#                 it+=1
#             rem=n-it
#             csum=sums
#             for _ in range(rem): csum|=csum<<x & mask
#             res.append(csum>>k & 1 == 1)
#         return res


# class Solution:
#     def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
#         nums.sort()
#         n=len(nums)
#         res=[]
#         sums=1
#         it=0
#         mask = (1 << (k + 1)) - 1  # keep only sums up to k
#         for x in range(1,n+1):
#             while it<n and nums[it]<=x:
#                 sums|=(sums<<x) & mask
#                 it+=1
#             rem=n-it
#             csum=sums
#             take = 1
#             while rem >= take:
#                 csum |= (csum << (take * x)) & mask
#                 rem -= take
#                 take <<= 1
#             csum |= (csum<<(rem*x)) & mask
#             res.append(csum>>k & 1 == 1)
#         return res

# class Solution:
#     def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        
#         n=len(nums)
#         cnt=Counter(nums)
#         sums,rcnt=1,0
#         mask=(1<<(k+1))-1
#         res=[]
#         for x in range(1,n+1):
#             for _ in range(cnt[x]):
#                 sums|=(sums<<x)&mask
#             rcnt+=cnt[x]
#             isums=sums
#             for _ in range(n-rcnt):
#                 isums|=(isums<<x)&mask
#             res.append((isums>>k & 1) ==1)
#         return res

# class Solution:
#     def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        
#         n=len(nums)
#         cnt=Counter(nums)
#         sums,rcnt=1,0
#         mask=(1<<(k+1))-1
#         res=[]

#         def bsplit(sums,x,times):
#             p=1
#             while times>=p:
#                 sums|=(sums<<(p*x))&mask
#                 times-=p
#                 p<<=1
#             sums|=(sums<<(times*x))&mask
#             return sums&mask

#         for x in range(1,n+1):
#             sums=bsplit(sums,x,cnt[x])
#             rcnt+=cnt[x]
#             isums=bsplit(sums,x,n-rcnt)
#             res.append((isums>>k & 1) ==1)
#         return res

# class Solution:
#     def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        
#         n=len(nums)
#         cnt=Counter(nums)
#         sums,rcnt=1,0
#         mask=(1<<(k+1))-1
#         res=[]

#         def bsplit(sums,x,times):
#             p=1
#             while times>=p:
#                 sums|=(sums<<(p*x))&mask
#                 times-=p
#                 p<<=1
#             sums|=(sums<<(times*x))&mask
#             return sums&mask

#         for x in range(1,n+1):
#             sums=bsplit(sums,x-1,cnt[x-1])
#             isums=bsplit(sums,x,n-rcnt)
#             rcnt+=cnt[x]
#             res.append((isums>>k & 1) ==1)
#         return res


class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        
        n=len(nums)
        cnt=Counter(nums)
        sums,rcnt=1,0
        mask=(1<<(k+1))-1
        res=[]

        def bsplit(sums,x,times):
            p=1
            while times>=p:
                sums|=(sums<<(p*x))&mask
                times-=p
                p<<=1
            sums|=(sums<<(times*x))&mask
            return sums

        for x in range(1,n+1):
            sums=bsplit(sums,x,cnt[x])
            rcnt+=cnt[x]
            isums=bsplit(sums,x,n-rcnt)
            res.append((isums>>k & 1) ==1)
        return res
# 0b1
# 0b10001
# 0b1000100010001
# 0b10001000100010001000100010001
# 0b100010001000100010001000100010001

# 4 4 4 4 4 4 4 4
# 4 8 16 4