# TLE
# class Solution:
#     def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
#         @cache
#         def isPrefixAndSuffix(str1, str2):
#             if len(str1)>len(str2): return False
#             m=len(str1)
#             return str2[:m]==str2[-m:]==str1

#         n,res=len(words),0
#         for i in range(n):
#             for j in range(i+1,n):
#                 if isPrefixAndSuffix(words[i],words[j]): res+=1
        
#         return res

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie=lambda: defaultdict(trie)
        root = trie()
        res = 0
        for w in words:
            x = root
            for k in zip(w, reversed(w)):
                x=x[k]
                res+=x.get(0, 0)
            x[0] = x.get(0, 0) + 1
        return res