# class Solution:

#     def __init__(self, nums: List[int]):
#         self.nums=nums
#         self.res=nums[:]

#     def reset(self) -> List[int]: return self.nums
        

#     def shuffle(self) -> List[int]:
#         shuffle(self.res)
#         return self.res


# # Your Solution object will be instantiated and called as such:
# # obj = Solution(nums)
# # param_1 = obj.reset()
# # param_2 = obj.shuffle()


class Solution:
    def __init__(self, nums):
        self.nums=nums

    def reset(self): return self.nums

    def shuffle(self):
        res=self.nums[:]
        n=len(res)
        for i in range(n):
            j = random.randint(i, n-1)
            res[i], res[j] =res[j],res[i]
        return res