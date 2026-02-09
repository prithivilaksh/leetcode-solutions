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

class MyCalendar:

    def __init__(self):
        self.intv=[]

    def book(self, s: int, e: int) -> bool:
        intv=self.intv
        i=bisect_right(intv,s,key=lambda x:x[0])
        l,r=i-1,i
        if 0<=l and s<intv[l][1]: return False
        if r<len(intv) and intv[r][0]<e: return False
        intv[r:r]=[[s,e]]
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)