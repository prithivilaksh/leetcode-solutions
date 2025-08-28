# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         cnt=defaultdict(int)
#         for x in nums:cnt[x]+=1
#         h,res=[],[]
#         for key,v in cnt.items():
#             heappush(h,(-v,key))
        
#         for _ in range(k):res.append(heappop(h)[1])
#         return res

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         cnt=defaultdict(int)
#         for x in nums:cnt[x]+=1
    
#         return [x for x,_ in sorted(cnt.items(),key=lambda x:x[1],reverse=True)[:k]]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        vcnt,h=defaultdict(int),[]
        for v in nums:vcnt[v]+=1

        for v,cnt in vcnt.items():
            heappush(h,(cnt,v))
            if len(h)>k:heappop(h)
        
        return [v for _,v in h]

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         n=len(nums)
#         vcnt=defaultdict(int)
#         for v in nums:vcnt[v]+=1

#         cntv=[[] for i in range(n)]
#         for v,cnt in vcnt.items():
#             cntv[cnt-1].append(v)
        
#         res=[]
#         for cnt in range(n-1,-1,-1):
#             for v in cntv[cnt]:
#                 res.append(v)
#                 if len(res)==k: return res
        