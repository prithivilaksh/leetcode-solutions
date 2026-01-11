## TLE
# class Solution:
#     def ladderLength(self, b: str, e: str, words: List[str]) -> int:

#         words.append(b)
#         m,n=len(words),len(b)
#         g=defaultdict(list)

#         def isadj(i,j):
#             return sum(int(a!=b) for a,b in zip(words[i],words[j]))==1

#         for i in range(m):
#             for j in range(i+1,m):
#                 if isadj(i,j):
#                     g[i].append(j)
#                     g[j].append(i)
        
#         dq=deque([m-1])
#         vis,dis=set([m-1]),1

#         while dq:
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 if words[u]==e: return dis
#                 for v in g[u]:
#                     if v not in vis:
#                         dq.append(v)
#                         vis.add(v)
#             dis+=1
#         return 0
                    

## TLE
# class Solution:
#     def ladderLength(self, b: str, e: str, words: List[str]) -> int:

#         words.append(b)
#         m,n=len(words),len(b)
#         g=defaultdict(list)

#         def isadj(i,j):
#             return sum(a!=b for a,b in zip(words[i],words[j]))==1

#         for i in range(m):
#             for j in range(i+1,m):
#                 if isadj(i,j):
#                     g[i].append(j)
#                     g[j].append(i)
        
#         dq=deque([m-1])
#         vis,dis=set([m-1]),1

#         while dq:
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 if words[u]==e: return dis
#                 while g[u]:
#                     v=g[u].pop()
#                     if v not in vis:
#                         dq.append(v)
#                         vis.add(v)
#             dis+=1
#         return 0


## TLE
# class Solution:
#     def ladderLength(self, b: str, e: str, words: List[str]) -> int:

#         m=len(words)
#         g=defaultdict(list)

#         def isadj(a,b):
#             return sum(a!=b for a,b in zip(a,b))==1
        
#         dq=deque([b])
#         vis,dis=set([b]),1

#         while dq:
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 if u==e: return dis
#                 for v in words:
#                     if v not in vis and isadj(u,v):
#                         dq.append(v)
#                         vis.add(v)
#             dis+=1
#         return 0



# class Solution:
#     def ladderLength(self, b: str, e: str, words: List[str]) -> int:
#         words=set(words)
#         if e not in words: return 0
#         words.add(b)
#         g=defaultdict(list)
#         n=len(b)

#         for word in words:
#             for i in range(n):
#                 pat=word[:i]+"_"+word[i+1:]
#                 g[pat].append(word)
        
#         dq=deque([b])
#         vis,dis=set(),1

#         while dq:
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 if u==e: return dis
#                 for i in range(n):
#                     pat=u[:i]+"_"+u[i+1:]
#                     for v in g[pat]:
#                         if v not in vis:
#                             dq.append(v)
#                             vis.add(v)
#             dis+=1
#         return 0


# class Solution:
#     def ladderLength(self, b: str, e: str, words: List[str]) -> int:
#         words=set(words)
#         if e not in words: return 0
#         words.add(b)
#         g=defaultdict(list)
#         n=len(b)

#         for word in words:
#             for i in range(n):
#                 pat=word[:i]+"_"+word[i+1:]
#                 g[pat].append(word)
        
#         dq=deque([b])
#         vis,dis=set(),1

#         while dq:
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 if u==e: return dis
#                 for i in range(n):
#                     pat=u[:i]+"_"+u[i+1:]
#                     while g[pat]:
#                         v=g[pat].pop()
#                         if v not in vis:
#                             dq.append(v)
#                             vis.add(v)
#             dis+=1
#         return 0

# class Solution:
#     def ladderLength(self, b: str, e: str, words: List[str]) -> int:
#         words=set(words)
#         if e not in words: return 0
#         words.add(b)
#         n=len(b)
        
#         dq=deque([b])
#         vis,dis=set(),1

#         while dq:
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 if u==e: return dis
#                 for i in range(n):
#                     for c in "abcdefghijklmnopqrstuvwxyz":
#                         v=u[:i]+c+u[i+1:]
#                         if v in words:
#                             dq.append(v)
#                             words.remove(v)
#             dis+=1
#         return 0
                   
                    
# class Solution:
#     def ladderLength(self, b: str, e: str, words: List[str]) -> int:
#         words=set(words)
#         if e not in words: return 0
#         words.add(b)
#         g=defaultdict(list)
#         n=len(b)

#         for word in words:
#             for i in range(n):
#                 pat=word[:i]+"_"+word[i+1:]
#                 g[pat].append(word)
        
#         dq=deque([b])
#         dis=1

#         while dq:
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 if u==e: return dis
#                 for i in range(n):
#                     pat=u[:i]+"_"+u[i+1:]
#                     while g[pat]:
#                         v=g[pat].pop()
#                         dq.append(v)
#             dis+=1
#         return 0


# class Solution:
#     def ladderLength(self, b: str, e: str, words: List[str]) -> int:


#         # idea/observation:
#         # 1) the core issue will be in building the graph
#         # 2) the naive approach will be N * N - check among all pairs to build the graph
#         # 3) we know that, there are only 26 possible values a-z and length of word <= 10
#         # 4) for each word, we can find which pattern it matches (atmost 10) and create an edge

#         words=set(words)
#         if e not in words: return 0
#         g=defaultdict(list)
#         n=len(b)

#         for word in words:
#             for j in range(n):
#                 pat=word[:j]+"_"+word[j+1:]
#                 g[pat].append(word)
        
#         dq,vis,dis=deque([b]),set([b]),1

#         while dq:
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 if u==e: return dis
#                 for j in range(n):
#                     pat=u[:j]+"_"+u[j+1:]
#                     while g[pat]:
#                         v=g[pat].pop()
#                         if v not in vis:
#                             vis.add(v)
#                             dq.append(v)
#             dis+=1
#         return 0


# class Solution:
#     def ladderLength(self, b: str, e: str, words: List[str]) -> int:

#         words=set(words+[b])
#         if e not in words: return 0

#         n=len(b)
#         mp=defaultdict(set)

#         for word in words:
#             for i in range(n):
#                 pat=word[:i]+"*"+word[i+1:]
#                 mp[pat].add(word)
        
#         dq,vis,d=deque([b]),set([b]),1

#         while dq:
#             d+=1
#             for _ in range(len(dq)):
#                 word=dq.popleft()
#                 for i in range(n):
#                     pat=word[:i]+"*"+word[i+1:]
#                     while mp[pat]:
#                         cand=mp[pat].pop()
#                         if cand not in vis:
#                             if cand==e: return d
#                             vis.add(cand)
#                             dq.append(cand)
#         return 0


class Solution:
    def ladderLength(self, b: str, e: str, words: List[str]) -> int:

        words=set(words+[b])
        if e not in words: return 0

        n=len(b)
        mp=defaultdict(set)

        for word in words:
            for i in range(n):
                pat=word[:i]+"*"+word[i+1:]
                mp[pat].add(word)
        
        bdq,edq,bvis,evis,d=deque([b]),deque([e]),set([b]),set([e]),1

        while bdq or edq:
            dq,vis=(bdq,bvis) if len(bdq)>len(edq) else (edq,evis)
            d+=1
            for _ in range(len(dq)):
                word=dq.popleft()
                for i in range(n):
                    pat=word[:i]+"*"+word[i+1:]
                    while mp[pat]:
                        cand=mp[pat].pop()
                        if cand not in vis:
                            vis.add(cand)
                            if cand in bvis and cand in evis: return d
                            dq.append(cand)
        return 0
        
