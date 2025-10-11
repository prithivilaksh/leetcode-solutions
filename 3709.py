# class ExamTracker:

#     def __init__(self):
#         self.arr=[(0,0)]

#     def record(self, time: int, score: int) -> None:
#         rscore=self.arr[-1][1]+score
#         self.arr.append((time,rscore))

#     def totalScore(self, startTime: int, endTime: int) -> int:
#         arr=self.arr
#         l=bisect_left(arr,(startTime,))
#         r=bisect_left(arr,(endTime,))
#         if arr[r][0]!=endTime: r-=1
#         res = arr[r][1]-arr[l-1][1]
#         return res


# # Your ExamTracker object will be instantiated and called as such:
# # obj = ExamTracker()
# # obj.record(time,score)
# # param_2 = obj.totalScore(startTime,endTime)

# class ExamTracker:

#     def __init__(self):
#         self.arr=[(0,0)]

#     def record(self, time: int, score: int) -> None:
#         rscore=self.arr[-1][1]+score
#         self.arr.append((time,rscore))

#     def totalScore(self, startTime: int, endTime: int) -> int:
#         arr=self.arr
#         l=bisect_left(arr,(startTime,))
#         r=bisect_right(arr,(endTime,inf))
#         res = arr[r-1][1]-arr[l-1][1]
#         return res


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)

class ExamTracker:

    def __init__(self):
        self.pre = [0]
        self.times = [0]

    def record(self, time: int, score: int) -> None:
        self.pre.append(score + self.pre[-1])
        self.times.append(time)

    def totalScore(self, startTime: int, endTime: int) -> int:
        i = bisect_left(self.times, startTime)
        j = bisect_right(self.times, endTime)
        return self.pre[j - 1] - self.pre[i - 1]