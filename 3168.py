class Solution:
    def minimumChairs(self, s: str) -> int:
        
        res=cnt=0
        for x in s:
            if x=="E": cnt+=1
            else: cnt-=1
            res=max(res,cnt)
        return res