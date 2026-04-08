# class Solution:
#     def canConstruct(self, s: str, k: int) -> bool:
        
#         if k>len(s): return False
#         cnt=Counter(s)
#         one=two=0
#         for c,count in cnt.items():
#             if count%2==1: one+=1
#             two+=count//2

#         if one>k: return False

#         return True

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        if k>len(s): return False
        if k==len(s) or k>=26: return True
        cnt,one=Counter(s),0
        for c,count in cnt.items():
            if count%2==1: one+=1

        if one>k: return False
        return True