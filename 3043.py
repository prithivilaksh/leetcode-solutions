# class Solution:
#     def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
#         trie=lambda:defaultdict(trie)

#         def add(node,word):
#             for x in word:
#                 node=node[x]
        
#         a,b=trie(),trie()
#         for w in set(arr1): add(a,str(w))
#         for w in set(arr2): add(b,str(w))

#         def dfs(a,b):
#             x,y=set(a.keys()),set(b.keys())
#             res=0
#             for k in x&y:
#                 res=max(res,1+dfs(a[k],b[k]))
#             return res
        
#         return dfs(a,b)

# class Solution:
#     def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
#         pre=set()
#         for w in map(str,arr1):
#             s=""
#             for c in w:
#                 s+=c
#                 pre.add(s)
        
#         res=0
#         for w in map(str,arr2):
#             s=""
#             for c in w:
#                 s+=c
#                 if s not in pre: break
#                 res=max(res,len(s))
#         return res


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        if len(arr1)<len(arr2):arr1,arr2=arr2,arr1
        pre=set()
        for w in map(str,set(arr1)):
            s=""
            for c in w:
                s+=c
                pre.add(s)
        
        res=0
        for w in map(str,set(arr2)):
            s=""
            for c in w:
                s+=c
                if s not in pre: break
                res=max(res,len(s))
        return res


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pre = set()
        for n in arr1:
            while n and n not in pre:
                pre.add(n)
                n //= 10

        res = 0
        for n in arr2:
            while n > res:
                if n in pre:
                    res = n
                    break
                n //= 10

        return 0 if res==0 else len(str(res))