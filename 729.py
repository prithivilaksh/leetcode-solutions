# class MyCalendar:

#     def __init__(self):
#         self.intv=[]
        

#     def book(self, s: int, e: int) -> bool:
#         intv=self.intv
#         i=bisect_right(intv,s,key=lambda x:x[0])
#         l,r=i-1,i
#         if 0<=l<len(intv) and s<intv[l][1]: return False
#         if 0<=r<len(intv) and intv[r][0]<e: return False
#         intv[r:r]=[[s,e]]
#         return True

        


# # Your MyCalendar object will be instantiated and called as such:
# # obj = MyCalendar()
# # param_1 = obj.book(startTime,endTime)

# class MyCalendar:

#     def __init__(self):
#         self.intv=[]

#     def book(self, s: int, e: int) -> bool:
#         intv=self.intv
#         i=bisect_right(intv,s,key=lambda x:x[0])
#         l,r=i-1,i
#         if 0<=l and s<intv[l][1]: return False
#         if r<len(intv) and intv[r][0]<e: return False
#         intv[r:r]=[[s,e]]
#         return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)


# class MyCalendar:

#     def __init__(self):
#         self.intvs=SortedList()

#     def book(self, s: int, e: int) -> bool:
#         pos=bisect_left(self.intvs,[s,e])
#         if pos-1>=0 and self.intvs[pos-1][1]>s: return False
#         if pos<len(self.intvs) and e>self.intvs[pos][0]: return False
#         self.intvs.add([s,e])
#         return True
        


# # Your MyCalendar object will be instantiated and called as such:
# # obj = MyCalendar()
# # param_1 = obj.book(startTime,endTime)

class MyCalendar:

    def __init__(self):
        self.intvs=[]

    def book(self, s: int, e: int) -> bool:
        pos=bisect_left(self.intvs,[s,e])
        if pos-1>=0 and self.intvs[pos-1][1]>s: return False
        if pos<len(self.intvs) and e>self.intvs[pos][0]: return False
        self.intvs[pos:pos]=[[s,e]]
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)