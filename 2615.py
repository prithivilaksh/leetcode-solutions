# class Solution:
#     def distance(self, nums: List[int]) -> List[int]:
        
#         #idea
#         # 1) for a given value sum up the distance from i to j for all j where nums[i]==nums[j]

#         # 1 _ 1 1 _ _ 1
#         # 0   2 3     6

#         ind,arr=defaultdict(list),[0]*len(nums)
#         for i,x in enumerate(nums): ind[x].append(i)

#         def distance(indices):
#             n,cnt,rsum=len(indices),1,0
#             for i in range(1,n):
#                 rsum+=cnt*abs(indices[i]-indices[i-1])
#                 arr[indices[i]]+=rsum
#                 cnt+=1

#         for indices in ind.values():
#             distance(indices);distance(indices[::-1])
#         return arr


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        #idea
        # 1) for a given value sum up the distance from i to j for all j where nums[i]==nums[j]

        # 1 _ 1 1 _ _ 1
        # 0   2 3     6

        ind,arr=defaultdict(list),[0]*len(nums)
        for i,x in enumerate(nums): ind[x].append(i)

        for indices in ind.values():
            n,tot,cnt,rsum=len(indices),sum(indices),0,0
            if n==1: continue
            for i in indices:
                arr[i]+= (cnt*i)-rsum
                arr[i]+= -((n-cnt)*i)+(tot-rsum)
                cnt+=1
                rsum+=i
        return arr


# 0 2 3 5

# 2 - 0
# 2 - 2
# -2 + 3
# -2 + 5


# class Solution:
#     def distance(self, nums: List[int]) -> List[int]:
        
#         #idea
#         # 1) for a given value sum up the distance from i to j for all j where nums[i]==nums[j]

#         # 1 _ 1 1 _ _ 1
#         # 0   2 3     6



#         n=len(nums)
#         arr=[0]*n
        
#         last,rsum,cnt={},defaultdict(int),defaultdict(int)
#         for i in range(n):
#             if nums[i] in last:
#                 rsum[nums[i]]+=cnt[nums[i]]*(i-last[nums[i]])
#                 arr[i]+=rsum[nums[i]]
#             last[nums[i]]=i
#             cnt[nums[i]]+=1

#         last,rsum,cnt={},defaultdict(int),defaultdict(int)
#         for i in range(n-1,-1,-1):
#             if nums[i] in last:
#                 rsum[nums[i]]+=cnt[nums[i]]*(last[nums[i]]-i)
#                 arr[i]+=rsum[nums[i]]
#             last[nums[i]]=i
#             cnt[nums[i]]+=1
        
#         return arr

        