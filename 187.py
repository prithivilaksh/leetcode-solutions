# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
#         n=len(s)
#         if n<=10: return []

#         res=defaultdict(int)
#         for i in range(n-10+1):
#             res[s[i:i+10]]+=1

#         return [k for k,v in res.items() if v>1]

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        n=len(s)
        if n<=10: return []

        res,seen=set(),set()
        for i in range(n-10+1):
            word=s[i:i+10]
            if word in seen: res.add(word)
            else: seen.add(word)

        return list(res)

