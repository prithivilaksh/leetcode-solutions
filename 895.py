class FreqStack:

    def __init__(self):
        self.freq=defaultdict(int)
        self.f2st=defaultdict(list)
        self.mxf=0
        
    def push(self, val: int) -> None:
        freq,f2st,mxf=self.freq,self.f2st,self.mxf
        freq[val]+=1
        f2st[freq[val]].append(val)
        if mxf<freq[val]:self.mxf=freq[val]
        
    def pop(self) -> int:
        freq,f2st,mxf=self.freq,self.f2st,self.mxf
        val=f2st[mxf].pop()
        freq[val]-=1
        if not f2st[mxf]:self.mxf-=1
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()