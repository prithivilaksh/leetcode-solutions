# class Solution:
#     def calculate(self, s: str) -> int:
        

#         res,num,sign=0,0,1
#         st=[]

#         for c in s:
#             if c=="-":
#                 res+=sign*num
#                 num,sign=0,-1
#             elif c=="+":
#                 res+=sign*num
#                 num,sign=0,1
#             elif c in "1234567890":
#                 num=num*10+int(c)
#             elif c=="(":
#                 st.append(res)
#                 st.append(sign)
#                 res,num,sign=0,0,1
#             elif c==")":
#                 res+=sign*num
#                 res*=st.pop()
#                 res+=st.pop()
#                 num,sign=0,1
        
#         if num: res+=sign*num
#         return res



class Solution:
    def calculate(self, s: str) -> int:
        

        res,num,sign=0,0,1
        st=[]

        for c in s:
            if c in "1234567890":
                num=num*10+int(c)
            elif c=="-":
                res+=sign*num
                num,sign=0,-1
            elif c=="+":
                res+=sign*num
                num,sign=0,1
            elif c=="(":
                st.append(res)
                st.append(sign)
                res,sign=0,1
            elif c==")":
                res+=sign*num
                res*=st.pop()
                res+=st.pop()
                num=0
        
        if num: res+=sign*num
        return res


