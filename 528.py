# ## More memory req MLE
# class Solution:

#     def __init__(self, w: List[int]):
#         self.arr=[]
#         for i,x in enumerate(w):
#             for _ in range(x):
#                 self.arr.append(i)

#     def pickIndex(self) -> int:
#         return random.choice(self.arr)


# # Your Solution object will be instantiated and called as such:
# # obj = Solution(w)
# # param_1 = obj.pickIndex()

# class Solution:

#     def __init__(self, w: List[int]):
#         self.w=w
#         self.n=len(w)
#         for i in range(1,self.n):
#             self.w[i]+=self.w[i-1]

#     def pickIndex(self) -> int:
#         s=random.randint(0,self.w[-1]-1)
#         return bisect.bisect_right(self.w,s)


# # Your Solution object will be instantiated and called as such:
# # obj = Solution(w)
# # param_1 = obj.pickIndex()

# class Solution:

#     def __init__(self, w: List[int]):
#         self.w=w
#         self.n=len(w)
#         self.w[0]-=1
#         for i in range(1,self.n):
#             self.w[i]+=self.w[i-1]

#     def pickIndex(self) -> int:
#         s=random.randint(0,self.w[-1])
#         return bisect.bisect_left(self.w,s)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


class Solution:

    # idea/observation
    # 1) w=[1,3,5]. out of sum(w) times, ith index should be returned w[i] times
    def __init__(self, w: List[int]):
        w[0]-=1
        for i in range(1,len(w)): w[i]+=w[i-1]
        self.w=w

    def pickIndex(self) -> int:
        x=random.randint(0,self.w[-1])
        return bisect_left(self.w,x)


