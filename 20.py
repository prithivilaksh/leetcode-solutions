class Solution:
    def isValid(self, s: str) -> bool:
        
        map={
                "}":"{",
                ")":"(",
                "]":"["
            }
        st=["b"]
        for c in s:
            if c in "({[": st.append(c)
            elif st[-1]==map[c]: st.pop()
            else: return False
        return len(st)==1 