


# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
#         wcnt=defaultdict(int)
#         for w in words:wcnt[w]+=1
        
#         words=sorted(set(words))
#         wp={word:-i for i,word in enumerate(words)}
#         h,res=[],[]
#         for w,cnt in wcnt.items():
#             heappush(h,(cnt,wp[w]))
#             if len(h)>k: heappop(h)
        
#         for _ in range(k):
#             _,p=heappop(h)
#             res.append(words[-p])
        
#         return res[::-1]

# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:

#         wcnt=Counter(words)
#         n,res=len(words),[]
#         cntw=[[] for _ in range(n+1)]
#         for w,cnt in wcnt.items():
#             cntw[cnt].append(w)
#         for cnt in range(n,0,-1):
#             for w in sorted(cntw[cnt]):
#                 res.append(w);k-=1
#                 if k==0: return res

# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
#         wcnt=Counter(words)
        
#         words=sorted(set(words))
#         wp={word:-i for i,word in enumerate(words)}
#         h,res=[],[]
#         for w,cnt in wcnt.items():
#             heappush(h,(cnt,wp[w]))
#             if len(h)>k: heappop(h)
        
#         for _ in range(k):
#             _,p=heappop(h)
#             res.append(words[-p])
        
#         return res[::-1]


# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
#         wcnt=Counter(words)
        
#         cntw=[(-cnt,w) for w,cnt in wcnt.items()]
#         heapify(cntw)

#         return [heappop(cntw)[1] for _ in range(k)]

# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
#         class DescWord():
#             def __init__(self,word):
#                 self.word=word
#             def __lt__(self,other):
#                 return self.word>other.word
#             def __eq__(self,other):
#                 return self.word==other.word
        
#         wcnt=Counter(words)
#         h=[]
#         for w,cnt in wcnt.items():
#             heappush(h,(cnt,DescWord(w)))
#             if len(h)>k: heappop(h)
        
#         return [heappop(h)[1].word for _ in range(k)][::-1]

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        class DescWord():
            def __init__(self,word,cnt):
                self.word=word
                self.cnt=cnt
            def __lt__(self,other):
                if self.cnt!=other.cnt: return self.cnt<other.cnt
                return self.word>other.word
            def __eq__(self,other):
                return self.cnt==other.cnt and self.word==other.word
        
        wcnt=Counter(words)
        h=[]
        for w,cnt in wcnt.items():
            heappush(h,DescWord(w,cnt))
            if len(h)>k: heappop(h)
        
        return [heappop(h).word for _ in range(k)][::-1]