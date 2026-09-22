class Solution:
    def placeWordInCrossword(self, board: list[list[str]], word: str) -> bool:
        
        n=len(word)
        def check(cand):
            for a,b in zip(word,cand):
                if b!=' ' and a!=b: return False
            return True

        for row in board:
            for cand in ''.join(row).split('#'):
                if len(cand)==n and (check(cand) or check(cand[::-1])): return True

        for col in zip(*board):
            for cand in ''.join(col).split('#'):
                if len(cand)==n and (check(cand) or check(cand[::-1])): return True
        
        return False