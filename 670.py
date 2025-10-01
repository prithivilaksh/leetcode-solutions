# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         ind={}
#         num=[int(i) for i in str(num)]
#         for i,x in enumerate(num): ind[x]=i

#         def get_result():
#             res,mul=0,1
#             while num:
#                 res+=mul*num.pop()
#                 mul*=10
#             return res

#         for i,x in enumerate(num):
#             for j in range(9,-1,-1):
#                 if j>x and j in ind and i<ind[j]:
#                     j=ind[j]
#                     num[i],num[j]=num[j],num[i]
#                     return get_result()
#         return get_result()

# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         ind={}
#         num=[int(i) for i in str(num)]
#         for i,x in enumerate(num): ind[x]=i

#         def get_result():
#             res,mul=0,1
#             while num:
#                 res+=mul*num.pop()
#                 mul*=10
#             return res

#         for i,x in enumerate(num):
#             for j in range(9,-1,-1):
#                 if j<=x: break
#                 if j in ind and i<ind[j]:
#                     j=ind[j]
#                     num[i],num[j]=num[j],num[i]
#                     return get_result()
#         return get_result()

# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         num=list(str(num))
#         ind={int(x):i for i,x in enumerate(num)}
#         print(ind)
#         for i,x in enumerate(num):
#             for j in range(9,int(x),-1):
#                 if j in ind and i<ind[j]:
#                     j=ind[j]
#                     num[i],num[j]=num[j],num[i]
#                     print(num)
#                     return int(''.join(num))
#         return int(''.join(num))

class Solution:
    def maximumSwap(self, num: int) -> int:
        num=[x for x in str(num)]
        n=len(num)
        mxi=l=r=n-1
        for i in range(n-1,-1,-1):
            if num[i]>num[mxi]: mxi=i
            if num[i]<num[mxi]: l,r=i,mxi
        num[l],num[r]=num[r],num[l]
        return int(''.join(num))
        
# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         # idea:
#         #     1) for every element from left to right, select the right most element which is greater than current 

#         num=[x for x in str(num)]
#         n=len(num)
#         for i in range(n):
#             mxi=i
#             for j in range(i+1,n):
#                 if num[mxi]<=num[j]: mxi=j
#             if num[i]!=num[mxi]:
#                 num[i],num[mxi]=num[mxi],num[i]
#                 break

#         return int(''.join(num))