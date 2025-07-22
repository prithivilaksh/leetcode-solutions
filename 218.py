class Solution:
    def getSkyline(self, b: List[List[int]]) -> List[List[int]]:
        
        
        xs=sorted([x for x,_,_ in b]+[x for _,x,_ in b])

        i,n=0,len(b)
        h,res=[],[[0,0]]
        for x in xs:
            while i<n and b[i][0]<=x:
                heappush(h,[-b[i][2],b[i][1]])
                i+=1
            
            while h and h[0][1]<=x:
                heappop(h)
            
            ch=-h[0][0] if h else 0
            if res[-1][1]!=ch: res.append([x,ch])
        
        return res[1:]
            
        
    
