class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ans = len(wordsDict)
        if word1 == word2:
            j = -1
            for i, w in enumerate(wordsDict):
                if w == word1:
                    if j != -1: # i != -1 too, so both words found
                        ans = min(ans, i - j)
                    j = i
        else: # re-use 243.Shortest Word Distance I
            i = j = -1
            for k, w in enumerate(wordsDict):
                if w == word1:
                    i = k
                if w == word2:
                    j = k
                if i != -1 and j != -1:
                    ans = min(ans, abs(i - j))
        return ans

##############

class Solution: # combine above if-else
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        posA = -1
        posB = -1
        minDistance = float("inf")

        for i in range(len(words)):
            word = words[i]

            if word == word1:
                posA = i
            elif word == word2:
                posB = i

            if posA != -1 and posB != -1 and posA != posB:
                minDistance = min(minDistance, abs(posA - posB))

            if word1 == word2:
                posB = posA

        return minDistance
