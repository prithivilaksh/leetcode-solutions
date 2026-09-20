class DetectSquares:

    def __init__(self):
        self.p=defaultdict(lambda : defaultdict(int))

    def add(self, point: list[int]) -> None:
        x,y=point
        self.p[x][y]+=1

    def count(self, point: list[int]) -> int:
        p=self.p
        x,y=point
        res=0
        for ny in self.p[x].keys():
            d=ny-y
            if d==0: continue
            res+=p[x][y+d]*p[x+d][y]*p[x+d][y+d]
            res+=p[x][y+d]*p[x-d][y]*p[x-d][y+d]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)