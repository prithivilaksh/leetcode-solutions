# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
        
#         nums=[i for i in range(1,n+1)]
#         res=""

#         while nums:
#             rem,pos=len(nums)-1,0

#             while k-math.factorial(rem)>0:
#                 k-=math.factorial(rem)
#                 pos+=1

#             res+=str(nums[pos])
#             nums.pop(pos)
        
#         return res


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1
        res = ""
        
        for i in range(n - 1, -1, -1):
            fact = math.factorial(i)
            index = k // fact
            k %= fact
            res+=nums.pop(index)
            
        return res