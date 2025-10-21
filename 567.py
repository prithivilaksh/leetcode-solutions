# # class Solution:
# #     def checkInclusion(self, s1: str, s2: str) -> bool:
        
# #         cnt=defaultdict(int)
# #         for c in s1: cnt[c]+=1

# #         discnt,tot,l=0,len(cnt),0
# #         for r,c in enumerate(s2):
# #             cnt[c]-=1
# #             if cnt[c]==0: discnt+=1
# #             while cnt[c]<0: 
# #                 cnt[s2[l]]+=1
# #                 if cnt[s2[l]]==1: discnt-=1
# #                 l+=1 
# #             if discnt==tot: return True
        
# #         return False

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
        
#         cnt=defaultdict(int)
#         for c in s1: cnt[c]+=1

#         discnt,l=len(cnt),0
#         for r,c in enumerate(s2):
#             cnt[c]-=1
#             if cnt[c]==0: discnt-=1
#             else:
#                 while cnt[c]<0: 
#                     cnt[s2[l]]+=1
#                     if cnt[s2[l]]==1: discnt+=1
#                     l+=1 
#             if discnt==0: return True
        
#         return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        cnt=defaultdict(int)
        for c in s1: cnt[c]+=1

        discnt,tot,l=0,len(cnt),0
        for r,c in enumerate(s2):
            cnt[c]-=1
            if cnt[c]==0: discnt+=1
            while cnt[c]<0: 
                cnt[s2[l]]+=1
                if cnt[s2[l]]==1: discnt-=1
                l+=1 
            if discnt==tot: return True
        
        return False

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
        
#         cnt1,cnt2,wz=[0]*26,[0]*26,len(s1)
#         map=lambda x: ord(x)-ord('a')
#         for c in s1: cnt1[map(c)]+=1

#         for r,c in enumerate(s2):
#             if r>=wz: cnt2[map(s2[r-wz])]-=1
#             cnt2[map(c)]+=1
#             if cnt1==cnt2: return True
#         return False

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
        
#         cnt,wz=[0]*26,len(s1)
#         map=lambda x: ord(x)-ord('a')
#         for c in s1: cnt[map(c)]+=1

#         for r,c in enumerate(s2):
#             if r>=wz: cnt[map(s2[r-wz])]+=1
#             cnt[map(c)]-=1
#             if all(x==0 for x in cnt): return True
#         return False