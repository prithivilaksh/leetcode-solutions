# class Solution:
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         words=set(words)
#         @cache
#         def isPresent(word):
#             if word in words: return True
#             n=len(word)
#             for i in range(1,n):
#                 if isPresent(word[:i]) and isPresent(word[i:]): return True

#         def isConcatWord(word):
#             n=len(word)
#             for i in range(1,n):
#                 if isPresent(word[:i]) and isPresent(word[i:]): return True

#         return list(filter(isConcatWord,words))

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words=set(words)
        @cache
        def isPresent(word):
            if word in words or isConcatWord(word): return True

        @cache
        def isConcatWord(word):
            for i in range(1,len(word)):
                if word[:i] in words and isPresent(word[i:]): return True

        return list(filter(isConcatWord,words))

# class Solution:
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         wordset = set(words)
#         output = []

#         def canForm(word):
#             if not word:
#                 return False

#             n = len(word)
#             dp = [False] * (n + 1)
#             dp[0] = True  # empty string can be formed trivially

#             for i in range(1, n + 1):
#                 for j in range(i):
#                     # if substring word[j:i] is in wordset and
#                     # the prefix word[:j] can be formed (dp[j] is True)
#                     # then word[:i] can be formed
#                     if dp[j] and word[j:i] in wordset:
#                         # to avoid counting the word itself, 
#                         # ensure i < n or j > 0
#                         if i < n or j > 0:
#                             dp[i] = True
#                             break

#             return dp[n]

#         for word in words:
#             wordset.remove(word)  # avoid using the word itself
#             if canForm(word):
#                 output.append(word)
#             wordset.add(word)

#         return output