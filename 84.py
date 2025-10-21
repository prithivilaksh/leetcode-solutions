class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        
        h=h+[0]
        res,st=0,[]
        for r,x in enumerate(h):
            while st and h[st[-1]]>x:
                m=st.pop()
                l=st[-1] if st else -1
                res=max(res,h[m]*(r-l-1))
            st.append(r)
        return res