# class Solution:
#     def customSortString(self, order: str, s: str) -> str:
        
#         priority=defaultdict(lambda:26)
#         for i,c in enumerate(order):priority[c]=i
#         return "".join(sorted(s,key=lambda x:priority[x]))


# class Solution:
#     def customSortString(self, order: str, s: str) -> str:
        
#         priority={c:i for i,c in enumerate(order)}
#         return "".join(sorted(s,key=lambda x:priority[x] if x in priority else -1))

class Solution:
    def customSortString(self, order: str, s: str) -> str:

        cnt,res=Counter(s),""
        for c in order:
            if c in cnt: 
                res+=c*cnt[c]
                del cnt[c]
        for c,x in cnt.items(): res+=c*x
        return res
