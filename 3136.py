# class Solution:
#     def isValid(self, word: str) -> bool:
#         if len(word)<3: return False
#         isVowel=isConsonant=False
#         for x in word:
#             if x.isalnum():
#                 if x in "aieouAEIOU": isVowel=True
#                 elif x.isalpha(): isConsonant=True
#             else: return False
#         return isVowel and isConsonant

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3: return False
        isVowel=isConsonant=False
        for x in word:
            if x.isalpha():
                if x in "aieouAEIOU": isVowel=True
                else: isConsonant=True
            elif not x.isdigit(): return False
        return isVowel and isConsonant