class Solution:
    def checkStraightLine(self, cs: List[List[int]]) -> bool:
        
        (x1,y1),(x2,y2)=cs[:2]

        for x,y in cs:
            if (y-y1)*(x2-x1) != (y2-y1)*(x-x1): return False
        return True


