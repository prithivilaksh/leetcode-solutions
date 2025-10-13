# class Solution:
#     def canSeePersonsCount(self, h: List[int]) -> List[int]:
        
#         # idea/observation:
#         #     1) i can see j if h[i+1]..h[j-1] is less than h[i] and h[j]
#         #     2) At any point, if h[i]>h[j] where i<j, then no one before i can see j
#         #     3) So pop the heights which are no longer required (all js) (Monotonically dcreasing stack)
#         #     4) find the position until which current height can see.(insertion point using bisect_left)
#         #     5) we can always see 1 more than insertion point, except the end.

#         n,st=len(h),deque([])
#         res=[0]*n
#         for i in range(n-1,-1,-1):
#             pos=bisect_right(st,h[i])
#             if pos==len(st):res[i]=pos
#             else: res[i]=pos+1
#             while st and h[i]>st[0]: st.popleft()
#             st.appendleft(h[i])
#         return res
        

# class Solution:
#     def canSeePersonsCount(self, h: List[int]) -> List[int]:
        
#         # idea/observation:
#         #     1) i can see j if h[i+1]..h[j-1] is less than h[i] and h[j]
#         #     2) At any point, if h[i]>h[j] where i<j, then no one before i can see j
#         #     3) So pop the heights which are no longer required (all js) (Monotonically dcreasing stack)
#         #     4) find the position until which current height can see.(insertion point using bisect_left)
#         #     5) we can always see 1 more than insertion point, except the end.

#         n,st=len(h),deque([])
#         res=[0]*n
#         for i in range(n-1,-1,-1):
#             pos=bisect_right(st,h[i])
#             res[i]=pos + int(pos!=len(st))
#             while st and h[i]>st[0]: st.popleft()
#             st.appendleft(h[i])
#         return res
        

# class Solution:
#     def canSeePersonsCount(self, h: List[int]) -> List[int]:
        
#         # idea/observation:
#         #     1) i can see j if h[i+1]..h[j-1] is less than h[i] and h[j]
#         #     2) At any point, if h[i]>h[j] where i<j, then no one before i can see j
#         #     3) So pop the heights which are no longer required (all js) (Monotonically dcreasing stack)
#         #     4) find the position until which current height can see.(insertion point using bisect_left)
#         #     5) we can always see 1 more than insertion point, except the end.

#         n,st=len(h),[]
#         res=[0]*n
#         for i in range(n-1,-1,-1):
#             cnt=0
#             while st and h[i]>st[-1]: cnt+=1;st.pop()
#             res[i]=cnt + (1 if st else 0)
#             st.append(h[i])
#         return res


class Solution:
    def canSeePersonsCount(self, h: List[int]) -> List[int]:
        
        # idea/observation:
        #     1) i can see j if h[i+1]..h[j-1] is less than h[i] and h[j]
        #     2) At any point, if h[i]>h[j] where i<j, then no one before i can see j
        #     3) So pop the heights which are no longer required (all js) (Monotonically dcreasing stack)
        #     4) find the position until which current height can see.(insertion point using bisect_left)
        #     5) we can always see 1 more than insertion point, except the end.

        n,st=len(h),[]
        res=[0]*n
        for i in range(n-1,-1,-1):
            while st and h[i]>st[-1]: res[i]+=1;st.pop()
            if st: res[i]+=1
            st.append(h[i])
        return res