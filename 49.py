# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         ss2strs=defaultdict(list)
#         for s in strs:
#             ss2strs["".join(sorted(s))].append(s)
        
#         return list(ss2strs.values())

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         tup2strs=defaultdict(list)
#         for s in strs:
#             cnt=[0]*26
#             for c in s: cnt[ord(c)-ord('a')]+=1
#             tup2strs[tuple(cnt)].append(s)
        
#         return list(tup2strs.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        h2strs=defaultdict(list)
        for word in strs:
            hash=1
            for c in word: 
                hash*=primes[ord(c)-ord('a')]
            h2strs[hash].append(word)
        
        return list(h2strs.values())