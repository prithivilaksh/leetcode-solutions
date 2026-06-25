# class Solution:

#     @cache
#     def countAndSay(self, n: int) -> str:
#         if n==1: return "1"
#         return self.runLengthEncoding(self.countAndSay(n-1))

#     @cache
#     def runLengthEncoding(self,s) -> int:
#         res=""
#         for x,g in groupby(s):
#             res+=str(len(tuple(g)))+str(x)
#         return res


# class Solution:
#     cache={1:"1"}
#     def countAndSay(self, n: int) -> str:
#         if n in Solution.cache: return Solution.cache[n]
        
#         curr="1"
#         for i in range(2,n+1):
#             next=""
#             for x,g in groupby(curr):
#                 next+=str(len(tuple(g)))+str(x)
#             Solution.cache[i]=curr=next
#         return Solution.cache[n]


class Solution:
    cache=defaultdict(str)

    @classmethod
    def init(cls):
        cls.cache[1]="1"
        for i in range(2,31):
            for x,g in groupby(cls.cache[i-1]):
                cls.cache[i]+=str(len(tuple(g)))+str(x)

    def countAndSay(self, n: int) -> str:
        if not self.__class__.cache: self.__class__.init()
        return self.__class__.cache[n]
        

