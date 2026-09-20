# class RLEIterator:

#     def __init__(self, encoding: list[int]):
#         self.encoding=encoding[::-1]

#     def next(self, n: int) -> int:
#         encoding=self.encoding
#         last=-1
#         while n and encoding:
#             exhaust=min(n,encoding[-1])
#             n-=exhaust
#             encoding[-1]-=exhaust
#             last=encoding[-2]
#             if encoding[-1]==0: 
#                 encoding.pop()
#                 encoding.pop()
#         return last if n==0 else -1



# # Your RLEIterator object will be instantiated and called as such:
# # obj = RLEIterator(encoding)
# # param_1 = obj.next(n)

class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.encoding=encoding
        self.i,self.n=0,len(encoding)

    def next(self, n: int) -> int:
        encoding=self.encoding
        
        while self.i<self.n:
            if n<=encoding[self.i]:
                encoding[self.i]-=n
                return encoding[self.i+1]
            n-=self.encoding[self.i]
            self.i+=2
        return -1



# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)