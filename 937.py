# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
#         ll,dl=[],[]
#         def isLL(x):
#             pos=x.find(" ")
#             c=x[pos+1]
#             return c.isalpha()

#         for l in logs:
#             if isLL(l): ll.append(l)
#             else: dl.append(l)
        
#         def comp(x):
#             pos=x.find(" ")
#             i=x[:pos]
#             c=x[pos:]
#             return c,i
        
#         ll.sort(key=comp)
#         return ll+dl

# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
#         ll,dl=[],[]

#         for l in logs:
#             if l[-1].isalpha(): ll.append(l)
#             else: dl.append(l)
        
#         def comp(x):
#             s=x.split(maxsplit=1)
#             return s[1],s[0]
        
#         ll.sort(key=comp)
#         return ll+dl


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def comp(x):
            i,c=x.split(maxsplit=1)
            return  (0,c,i) if x[-1].isalpha() else (1,)
        
        logs.sort(key=comp)
        return logs