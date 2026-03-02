# class Solution:
#     def asteroidCollision(self, nums: List[int]) -> List[int]:
#         st=[]
#         for x in nums:
#             while st and st[-1]>0 and x<0:
#                 y=st.pop()
#                 xabs,yabs=abs(x),abs(y)
#                 if yabs>xabs: x=y
#                 elif yabs==xabs: x=0
#             if x!=0: st.append(x)
        
#         return st


class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        st=[]
        for x in nums:
            while st and x<0 and st[-1]>0:
                y=st.pop()
                if y>-x: x=y
                elif y==-x: x=0
            if x!=0: st.append(x)
        
        return st