# class Solution:
#     def goodDaysToRobBank(self, sec: List[int], time: int) -> List[int]:
        
#         n=len(sec)
#         l,r=[0]*n,[0]*n
        
#         st=[-inf]
#         for i in range(n):
#             if st[-1]>=sec[i]:
#                 l[i]=len(st)
#                 st.append(sec[i])
#             else: st=[sec[i]]

#         st=[-inf]
#         for i in range(n-1,-1,-1):
#             if st[-1]>=sec[i]:
#                 r[i]=len(st)
#                 st.append(sec[i])
#             else: st=[sec[i]]
        
#         res=[]
#         for i in range(n):
#             if l[i]>=time<=r[i]: res.append(i)
#         return res


class Solution:
    def goodDaysToRobBank(self, nums: List[int], time: int) -> List[int]:
        
        n=len(nums)
        res=[]

        dec=inc=0
        p1,p2=-inf,inf
        for i in range(n-time):
            if p1>=nums[i]: dec+=1
            else: dec=0

            if p2<=nums[i+time]: inc+=1
            else: inc=0

            p1,p2=nums[i],nums[i+time]

            if inc>=time<=dec: res.append(i)
        return res
