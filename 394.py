# class Solution:
#     def decodeString(self, s: str) -> str:
        
#         st=[]
#         for c in s:
#             if c.isalpha():
#                 if st and st[-1].isalpha(): st[-1]+=c
#                 else: st.append(c)
#             elif c.isnumeric():
#                 if st and st[-1].isnumeric(): st[-1]+=c
#                 else: st.append(c)
#             elif c=='[': st.append("[")
#             else: #c==']'
#                 cstr=st.pop()
#                 st.pop()
#                 cnum=int(st.pop())
#                 if st and st[-1].isalpha(): st[-1]+=cstr*cnum
#                 else: st.append(cstr*cnum)
        
#         return ''.join(st)


# class Solution:
#     def decodeString(self, s: str) -> str:
        
#         st=[""]
#         for c in s:
#             if c.isalpha():
#                 if st[-1].isalpha(): st[-1]+=c
#                 else: st.append(c)
#             elif c.isnumeric():
#                 if st[-1].isnumeric(): st[-1]+=c
#                 else: st.append(c)
#             elif c=='[': st.append("[")
#             else: #c==']'
#                 cstr=st.pop()
#                 st.pop()
#                 cnum=int(st.pop())
#                 if st[-1].isalpha(): st[-1]+=cstr*cnum
#                 else: st.append(cstr*cnum)
        
#         return ''.join(st)


class Solution:
    def decodeString(self, s: str) -> str:
        
        st=[""]
        for c in s:
            if c=="]":
                cstr,cnum="",""
                while st[-1].isalpha(): cstr=st.pop()+cstr
                st.pop()
                while st[-1].isdigit(): cnum=st.pop()+cnum
                st.append(cstr*int(cnum))
            else: st.append(c)
        
        return ''.join(st)