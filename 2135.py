# class Solution:
#     def wordCount(self, startWords: list[str], targetWords: list[str]) -> int:
        
#         # idea:
#         # 1) add a new char to start & jumble to form target

#         def convert(s):
#             b=0
#             for c in s:
#                 x=ord(c)-ord('a')
#                 b|=1<<x
#             return b
        
#         targets,res=defaultdict(int),0
#         for t in targetWords:
#             targets[convert(t)]+=1
        
#         for s in startWords:
#             b=convert(s)
#             for i in range(26):
#                 if b>>i&1: continue
#                 cand=b|(1<<i)
#                 if targets[cand]>0:
#                     res+=targets[cand]
#                     targets[cand]=0

#         return res


class Solution:
    def wordCount(self, startWords: list[str], targetWords: list[str]) -> int:
        
        # idea:
        # 1) add a new char to start & jumble to form target

        mp={chr(ord('a')+i):i for i in range(26)}

        def convert(s):
            b=0
            for c in s:
                b|=1<<mp[c]
            return b
        
        starts,res=set(),0
        for s in startWords:
            starts.add(convert(s))
        
        for t in targetWords:
            b=convert(t)
            for c in t:
                if b^(1<<mp[c]) in starts:
                    res+=1
                    break

        return res


