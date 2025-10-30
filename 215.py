# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         h=[]
#         for x in nums:
#             heappush(h,x)
#             if len(h)>k: heappop(h)
#         return h[0]

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         def quick(l,r,k):
            
#             pos,piv,cnt=l,nums[r],1
#             for i in range(l,r):
#                 if nums[i]>=piv:
#                     cnt+=nums[i]==piv
#                     nums[pos],nums[i]=nums[i],nums[pos]
#                     pos+=1
#             nums[pos],nums[r]=nums[r],nums[pos]
#             if pos-l+1-cnt<k<=pos-l+1: return piv
#             elif pos-l+1<k: return quick(pos+1,r,k-(pos-l+1))
#             else: return quick(l,pos-1,k)

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         def quick(l,r):
            
#             pos,piv,cnt=l,nums[r],1
#             for i in range(l,r):
#                 if nums[i]>=piv:
#                     cnt+=nums[i]==piv
#                     nums[pos],nums[i]=nums[i],nums[pos]
#                     pos+=1
#             nums[pos],nums[r]=nums[r],nums[pos]
#             if pos-cnt<k<=pos: return piv
#             elif pos<k: return quick(pos+1,r)
#             else: return quick(l,pos-1)
#         k-=1
#         return quick(0,len(nums)-1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quick(arr,k):
            
            piv=random.choice(arr)
            l,m,r=[],[],[]
            for x in arr:
                if x>piv:l.append(x)
                elif x<piv:r.append(x)
                else: m.append(x)
            
            if k<=len(l): return quick(l,k)
            elif k<=len(l)+len(m): return piv
            else: return quick(r,k-len(l)-len(m))

        return quick(nums,k)