# class Solution(object):
#     def processStr(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """

#         res=""
#         for c in s:
#             if c=="*": res=res[:-1]
#             elif c=="#": res+=res
#             elif c=="%": res=res[::-1]
#             else: res+=c
#         return res
        
class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """

        res=[]
        for c in s:
            if c=="*": 
                if res: res.pop()
            elif c=="#": res.extend(res)
            elif c=="%": res=res[::-1]
            else: res.append(c)
        return ''.join(res)
        