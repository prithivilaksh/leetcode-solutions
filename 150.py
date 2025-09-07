
#int division rounds towards 0 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for x in tokens:
            if x in "+-*/":
                b,a=st.pop(),st.pop()
                if x=="+": res=a+b
                elif x=="-": res=a-b
                elif x=="*": res=a*b
                # else: res=floor(a/b) if a/b >=0 else ceil(a/b)
                else: res=int(a/b)
                st.append(res)
            else: st.append(int(x))

        return st[-1]
