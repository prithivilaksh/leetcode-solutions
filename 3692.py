# class Solution:
#     def majorityFrequencyGroup(self, s: str) -> str:
#         c2cnt=defaultdict(int)
#         cnt2c=defaultdict(str)
        
#         for c in s:c2cnt[c]+=1

#         for c,cnt in c2cnt.items():
#             cnt2c[cnt]+=c

#         res=""
#         for cnt,s in sorted(cnt2c.items(),reverse=True):
#             if len(s)>len(res):
#                 res=s
#         return res            

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        c2cnt=defaultdict(int)
        cnt2c=defaultdict(str)
        
        for c in s:c2cnt[c]+=1

        for c,cnt in c2cnt.items():
            cnt2c[cnt]+=c

        res1,res2="",0
        for cnt,s in cnt2c.items():
            if len(s)>len(res1) or len(s)==len(res1) and res2<cnt:
                res1,res2=s,cnt
        return res1            