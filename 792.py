# class Solution:
#     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
#         n=len(s)
#         ind=defaultdict(list)
#         for i,c in enumerate(s):
#             ind[c].append(i)
        
#         @cache
#         def indFrom(pos,c):
#             indlist=ind[c]
#             pos=bisect_left(indlist,pos)
#             return -1 if pos==len(indlist) else indlist[pos]
        
#         def isSubSeq(word):
#             pos=-1
#             for c in word:
#                 pos=indFrom(pos+1,c)
#                 if pos==-1: return False
#             return True
        
#         return sum(isSubSeq(word) for word in words)

# class Solution:
#     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
#         def isSubSeq(word):
#             i=-1
#             for c in word:
#                 i=s.find(c,i+1)
#                 if i==-1: return False
#             return True
        
#         return sum(isSubSeq(word) for word in words)

class Solution:

    def numMatchingSubseq(self, S, words):
        waiting = defaultdict(list, {' ': map(iter, words)})
        for c in ' ' + S:
            for it in waiting.pop(c,()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])