class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        
        a,b=rounds[0],rounds[-1]
        if a<=b: return list(range(a,b+1))
        return list(range(1,b+1)) + list(range(a,n+1))