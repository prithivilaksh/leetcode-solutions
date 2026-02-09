# class Solution:
#     def judgePoint24(self, cards: List[int]) -> bool:

#         def backtrack(cards):
#             if len(cards)==1: return abs(cards[0]-24)<1e-6

#             n=len(cards)
#             for i in range(n):
#                 for j in range(n):
#                     if i==j: continue

#                     a,b=cards[i],cards[j]
#                     ncards=[cards[k] for k in range(n) if k!=i and k!=j ]
                    
#                     if backtrack(ncards+[a-b]): return True
#                     if backtrack(ncards+[a+b]): return True
#                     if backtrack(ncards+[a*b]): return True
#                     if b!=0 and backtrack(ncards+[a/b]): return True

#             return False

#         return backtrack(cards)


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        def backtrack(cards):
            if len(cards)==1: return abs(cards[0]-24)<1e-6

            n=len(cards)
            for i in range(n):
                for j in range(i+1,n):

                    a,b=cards[i],cards[j]
                    ncards=[cards[k] for k in range(n) if k!=i and k!=j]
                    
                    if backtrack(ncards+[a-b]): return True
                    if backtrack(ncards+[b-a]): return True
                    if backtrack(ncards+[a+b]): return True
                    if backtrack(ncards+[a*b]): return True
                    if b!=0 and backtrack(ncards+[a/b]): return True
                    if a!=0 and backtrack(ncards+[b/a]): return True
                    
            return False

        return backtrack(cards)


