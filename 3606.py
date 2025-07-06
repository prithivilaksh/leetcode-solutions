# class Solution:
#     def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

#         res=[]
#         n=len(code)
#         for i in range(n):
#             if isActive[i] and code[i] and businessLine[i] in ('electronics','grocery','pharmacy','restaurant'):
#                 f=True
#                 for x in code[i]:
#                     if not x.isalnum() and x!="_":
#                         f=False;break
#                 if f: res.append([businessLine[i],code[i]])

#         res.sort()
#         return [c for b,c in res]
                
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        res=[]
        for i in range(len(code)):
            if isActive[i] and code[i] and businessLine[i] in ('electronics','grocery','pharmacy','restaurant'):
                if all(c.isalnum() or c=="_"   for c in code[i]):
                    res.append([businessLine[i],code[i]])

        res.sort()
        return [c for b,c in res]
                





        