# class Solution:
#     def minSwaps(self, s: str) -> int:

#         # idea/observation:
#         #     1) once we remove all the matching [], the resulting s will be like ][ or ]][[ or ]]][[[ or ]]]][[[[ etc.
#         #     2) for ][ and ]][[, the number of swaps is 1 (for 2 and 4, res=1)
#         #     3) for ]]][[[ and ]]]][[[[, the number of swaps is 2 (for 6 and 8, res=2)
#         #     4) the pattern is ceil(no of mistmatches/4)
        
#         st=[]
#         for c in s:
#             if st and st[-1]=="[" and c=="]": st.pop()
#             else: st.append(c)
        
#         return ceil(len(st)/4)


class Solution:
    def minSwaps(self, s: str) -> int:

#         # idea/observation:
#         #     1) once we remove all the matching [], the resulting s will be like ][ or ]][[ or ]]][[[ or ]]]][[[[ etc.
#         #     2) for ][ and ]][[, the number of swaps is 1 (for 2 and 4, res=1)
#         #     3) for ]]][[[ and ]]]][[[[, the number of swaps is 2 (for 6 and 8, res=2)
#         #     4) the pattern is ceil(no of mistmatches/4)
#         #     5) since no of [ is same as ], it is enough to track only one of them
#         #     6) whenever open>0(last char is [ ) and current char is ], decrement open
#         #     7) if current char is [, increment open
#         #     8) we are basically tracking number of unclosed [
#         #     9) so the result is ceil(no of unclosed [ /2)
        
        open=0
        for c in s:
            if c=="[": open+=1
            elif open>0: open-=1
        return ceil(open/2)