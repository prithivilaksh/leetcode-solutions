class Solution:
    def maxSubarrays(self, n: int, cp: List[List[int]]) -> int:
        
        left=defaultdict(list)
        for a,b in cp: left[max(a,b)].append(min(a,b))

        res,window,extra=0,[0,0],[0]*(n+1)
        for r in range(1,n+1):
            
            for l in left[r]:
                if l>window[1]: window=[window[1],l]
                elif l>window[0]: window=[l,window[1]]
            
            res+=r-window[1]
            extra[window[1]]+=window[1]-window[0]
        
        return res+max(extra)
