# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         # 1 2 3 4

#         # 1 2 4 3

#         # 1 3 2 4

#         # 1 3 4 2

#         # 1 4 2 3

#         # 1 4 3 2

#         # 2 1 3 4

#         # 2 1 4 3

#         # 2 3 1 4

#         # 2 3 4 1

#         # 2 4 1 3

#         # 2 4 3 1

#         # 3 1 2 4

#         # 3 1 4 2

#         # 3 2 1 4

#         # 3 2 4 1

#         # 3 4 1 2

#         # 3 4 2 1

#         # 4 1 2 3

#         # 4 1 3 2

#         # 4 2 1 3

#         # 4 2 3 1

#         # 4 3 1 2

#         # 4 3 2 1


#         # 4*3*2*1

#         n=len(nums)
#         l=-1

#         for i in range(n-2,-1,-1):
#             if nums[i]<nums[i+1]:
#                 l=i
#                 break

#         if l==-1: nums[:]=nums[::-1];return
        
#         for i in range(l+1,n):
#             if nums[l]>=nums[i]: break
#             r=i
        
#         nums[l],nums[r]=nums[r],nums[l]
#         nums[l+1:]=nums[l+1:][::-1]

# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         # 1 2 3 4

#         # 1 2 4 3

#         # 1 3 2 4

#         # 1 3 4 2

#         # 1 4 2 3

#         # 1 4 3 2

#         # 2 1 3 4

#         # 2 1 4 3

#         # 2 3 1 4

#         # 2 3 4 1

#         # 2 4 1 3

#         # 2 4 3 1

#         # 3 1 2 4

#         # 3 1 4 2

#         # 3 2 1 4

#         # 3 2 4 1

#         # 3 4 1 2

#         # 3 4 2 1

#         # 4 1 2 3

#         # 4 1 3 2

#         # 4 2 1 3

#         # 4 2 3 1

#         # 4 3 1 2

#         # 4 3 2 1


#         # 4*3*2*1

#         n=len(nums)
#         l=-1

#         for i in range(n-2,-1,-1):
#             if nums[i]<nums[i+1]:
#                 l=i
#                 break

#         if l==-1: nums[:]=nums[::-1];return
        
#         for i in range(n-1,l,-1):
#             if nums[l]<nums[i]: 
#                 r=i
#                 break
        
#         nums[l],nums[r]=nums[r],nums[l]
#         nums[l+1:]=nums[l+1:][::-1]




class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n=len(nums)
        st=[n-1]
        for i in range(n-2,-1,-1):
            if nums[i]>=nums[st[-1]]:
                st.append(i)
            else:
                j=st[-1]
                while st and nums[i]<nums[st[-1]]:
                    j=st.pop()
                nums[i],nums[j]=nums[j],nums[i]
                nums[i+1:]=nums[i+1:][::-1]
                return

        nums[:]=nums[::-1]


# 1 3 2



# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2

# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# 2 4 3 1




















