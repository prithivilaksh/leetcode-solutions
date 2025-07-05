class Solution:
    def partitionString(self, s: str) -> List[str]:

        seg,seen,st="",[],set()

        for c in s:
            
            seg+=c
            if seg not in st:
                seen.append(seg)
                st.add(seg)
                seg=""
                
        return seen
            
            
                
        