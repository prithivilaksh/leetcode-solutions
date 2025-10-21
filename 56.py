class Solution:
    def merge(self, ints: List[List[int]]) -> List[List[int]]:
        
        ints.sort(key=lambda x:x[0])
        res=[ints[0]]

        for s,e in ints[1:]:
            if res[-1][1]>=s:res[-1][1]=max(res[-1][1],e)
            else: res.append([s,e])
        
        return res