# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
        
#         mi,mx=deque(),deque()
#         res=l=0
#         for r,x in enumerate(nums):

#             while mi and mi[-1][0]>x: mi.pop()
#             mi.append((x,r))

#             while mx and mx[-1][0]<x: mx.pop()
#             mx.append((x,r))

#             while mx[0][0]-mi[0][0]>limit:
#                 if mi[0][1]<=mx[0][1]: _,j=mi.popleft()
#                 else: _,j=mx.popleft()
#                 l=j+1
            
#             res=max(res,r-l+1)
#         return res

# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:

#         max_d = deque()
#         min_d = deque()
#         left = 0
#         result = 0

#         for right, num in enumerate(nums):
#             while max_d and num > max_d[-1]:
#                 max_d.pop()
#             max_d.append(num)

#             while min_d and num < min_d[-1]:
#                 min_d.pop()
#             min_d.append(num)

#             while max_d[0] - min_d[0] > limit:
#                 if nums[left] == max_d[0]:
#                     max_d.popleft()
#                 if nums[left] == min_d[0]:
#                     min_d.popleft()
#                 left += 1

#             result = max(result, right - left + 1)

#         return result

        

# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:

#         mi,mx=deque(),deque()
#         l=res=0
#         for r,x in enumerate(nums):
#             while mi and mi[-1]>x: mi.pop()
#             mi.append(x)
            
#             while mx and mx[-1]<x: mx.pop()
#             mx.append(x)

#             while mx[0]-mi[0]>limit:
#                 if nums[l]==mx[0]: mx.popleft()
#                 if nums[l]==mi[0]: mi.popleft()
#                 l+=1
#             res=max(res,r-l+1)
#         return res

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        mi,mx=deque(),deque()
        l=res=0
        for r,x in enumerate(nums):
            while mi and nums[mi[-1]]>=x: mi.pop()
            mi.append(r)
            
            while mx and nums[mx[-1]]<=x: mx.pop()
            mx.append(r)

            while nums[mx[0]]-nums[mi[0]]>limit:
                if mx[0]==l: mx.popleft()
                if mi[0]==l: mi.popleft()
                l+=1
            res=max(res,r-l+1)
        return res



















        
            



