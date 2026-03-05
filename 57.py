class Solution:
    def insert(self, intvs: List[List[int]], nintv: List[int]) -> List[List[int]]:
        s,e=nintv
        n=len(intvs)

        l=bisect_left(intvs,s,key=lambda x:x[0])
        if l-1>=0 and intvs[l-1][1]>=s:
            s=intvs[l-1][0]
            l-=1
        
        r=bisect_left(intvs,e,key=lambda x:x[1])
        if r<n and intvs[r][0]<=e:
            e=intvs[r][1]
            r+=1

        intvs[l:r]=[[s,e]]
        return intvs
