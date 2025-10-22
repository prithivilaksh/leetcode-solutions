# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
        
#         st=[("b",-1)]
#         for i,c in enumerate(s):
#             if c==")" and st[-1][0]=="(": st.pop()
#             else: st.append((c,i))
#         st.append(("e",len(s)))
        
#         res=0
#         for i in range(1,len(st)):
#             res=max(res,st[i][1]-st[i-1][1]-1)
        
#         return res

# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
        
#         st,res=[("b",-1)],0
#         for i,c in enumerate(s):
#             if c==")" and st[-1][0]=="(": 
#                 st.pop()
#                 res=max(res,i-st[-1][1])
#             else: st.append((c,i))
#         res=max(res,len(s)-st[-1][1]-1)
#         return res

# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
        
#         st,res=[("b",-1)],0
#         for i,c in enumerate(s):
#             if c==")" and st[-1][0]=="(": 
#                 st.pop()
#                 res=max(res,i-st[-1][1])
#             else: st.append((c,i))

#         return res

# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
        
#         st,res=[-1],0
#         for i,c in enumerate(s):
#             if len(st)>1 and c==")" and s[st[-1]]=="(": 
#                 st.pop()
#                 res=max(res,i-st[-1])
#             else: st.append(i)

#         return res

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        st,res=[-1],0
        for i,c in enumerate(s):
            if c==")": 
                st.pop()
                if st: res=max(res,i-st[-1])
                else: st.append(i)
            else: st.append(i)

        return res