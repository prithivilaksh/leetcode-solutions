class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        # idea/observation:
        #     1) if a char is smaller than the previous char, we can always pop the prev char as long as the same char is present in the right side

        lsti={c:i for i,c in enumerate(s)}
        st,seen=[],set()

        for i,c in enumerate(s):
            if c in seen: continue
            while st and st[-1]>c and i<lsti[st[-1]]:
                seen.remove(st.pop())
            seen.add(c)
            st.append(c)
        
        return "".join(st)