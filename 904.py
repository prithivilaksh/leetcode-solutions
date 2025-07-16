# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
        
#         cnt,i,dist,res=defaultdict(int),0,0,0
#         for j,x in enumerate(fruits):
#             cnt[x]+=1
#             if cnt[x]==1: dist+=1
#             while dist>2:
#                 cnt[fruits[i]]-=1
#                 if cnt[fruits[i]]==0: dist-=1
#                 i+=1
#             res=max(res,j-i+1)
#         return res

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        cnt,i={},0
        for j,x in enumerate(fruits):
            cnt[x]=cnt.get(x,0)+1
            if len(cnt)>2:
                cnt[fruits[i]]-=1
                if cnt[fruits[i]]==0: del cnt[fruits[i]]
                i+=1
        return j-i+1