class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:


        # idea/observation:
        # 1) find all the available workers ready to move to left at that instant
        # 2) find all the available workers ready to move to right at that instant
        # 3) pop the least effecient worker from avlbl in the right and push to unavlb in the left
        # 4) else pop the least effecient worker from avlbl in the left and push to unavlbl in the right
        
        la,ra=[],[]
        lu,ru=[],[]

        for i,(tr,pk,tl,pt) in enumerate(time): heappush(la,(-(tl+tr),-i))
        
        t=0
        while True:
            
            while lu and lu[0][0]<=t:
                i=-heappop(lu)[1]
                tr,pk,tl,pt=time[i]
                heappush(la,(-(tl+tr),-i))

            while ru and ru[0][0]<=t:
                i=-heappop(ru)[1]
                tr,pk,tl,pt=time[i]
                heappush(ra,(-(tl+tr),-i))
            
            if ra:
                i=-heappop(ra)[1]
                tr,pk,tl,pt=time[i]
                heappush(lu,(t+tl+pt,-i))
                t+=tl
                n-=1
                if n==0: return t
            
            elif la and n>len(ru)+len(ra):
                i=-heappop(la)[1]
                tr,pk,tl,pt=time[i]
                heappush(ru,(t+tr+pk,-i))
                t+=tr
                
            elif lu or ru:
                mi=inf
                if lu: mi=min(mi,lu[0][0])
                if ru: mi=min(mi,ru[0][0])
                t=mi


