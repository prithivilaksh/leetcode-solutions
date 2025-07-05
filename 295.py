# class MedianFinder:

#     def __init__(self):
#         self.l,self.r=[],[]

#     def addNum(self, num: int) -> None:
#         num=-heapq.heappushpop(self.l,-num)
#         num=heapq.heappushpop(self.r,num)
#         if len(self.l)==len(self.r):heapq.heappush(self.l,-num)
#         else: heapq.heappush(self.r,num)

        
#     def findMedian(self) -> float:
#         if len(self.l)==len(self.r): return (-self.l[0]+self.r[0])/2
#         return -self.l[0]
        


# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()


class MedianFinder:

    def __init__(self):
        self.l,self.r=[],[]

    def addNum(self, num: int) -> None:
        
        if len(self.l)==len(self.r):
            num=heapq.heappushpop(self.r,num)
            heapq.heappush(self.l,-num)
        else: 
            num=-heapq.heappushpop(self.l,-num)
            heapq.heappush(self.r,num)

        
    def findMedian(self) -> float:
        if len(self.l)==len(self.r): return (-self.l[0]+self.r[0])/2
        return -self.l[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()