# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
        
#         n,res=len(s),[]
#         first,last=defaultdict(int),defaultdict(int)
#         for i,c in enumerate(s): last[c]=i
#         for i,c in enumerate(s[::-1]): first[c]=n-i-1
        
#         mi=mx=0
#         for i,c in enumerate(s):
#             mx=max(mx,last[c])
#             mi=min(mi,first[c])
#             if mx==i:
#                 res.append(mx-mi+1)
#                 mi=mx=i+1

#         return res


# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
        
#         n,res=len(s),[]
#         last=defaultdict(int)
#         for i,c in enumerate(s): last[c]=i
        
#         start=mx=0
#         for i,c in enumerate(s):
#             mx=max(mx,last[c])
#             if mx==i:
#                 res.append(mx-start+1)
#                 start=mx=i+1
                
#         return res


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last={c:i for i,c in enumerate(s)}
        res=[]
        start=mx=0
        for i,c in enumerate(s):
            mx=max(mx,last[c])
            if mx==i:
                res.append(mx-start+1)
                start=i+1
                
        return res

