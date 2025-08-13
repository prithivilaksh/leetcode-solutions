# class Solution:
#     def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
#         cnt=defaultdict(int)
#         for x in nums:cnt[x]+=1
#         for i in sorted(cnt):
#             if cnt[i]!=0:
#                 for j in range(i+k-1,i,-1):
#                     cnt[j]-=cnt[i]
#                     if cnt[j]<0: return False
#             del cnt[i]

#         return True

# class Solution:
#     def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
#         if len(nums)%k!=0: return False

#         cnt=defaultdict(int)
#         for x in nums:cnt[x]+=1
#         for r in nums:
#             if cnt[r]==0: continue
#             l=r
#             while cnt[l-1]:l-=1
#             for i in range(l,r+1):
#                 if cnt[i]==0: continue
#                 for j in range(i+k-1,i-1,-1):
#                     cnt[j]-=cnt[i]
#                     if cnt[j]<0: return False

#         return True


class Solution:
    def isPossibleDivide(self, nums: List[int], sz: int) -> bool:
        
        cnt,dq,opened=defaultdict(int),deque(),0
        for x in nums:cnt[x]+=1
        for k in sorted(cnt):
            if opened>cnt[k] or opened>0 and prev+1!=k: return False
            dq.append(cnt[k]-opened) # new beginning
            prev,opened=k,cnt[k]
            if len(dq)==sz: opened-=dq.popleft()
        return opened==0