class Solution:
    def minInterval(self, ivals: List[List[int]], qs: List[int]) -> List[int]:

        n=len(ivals)
        ivals.sort()

        h,i,res=[],0,defaultdict(lambda:-1)
        size = lambda x: x[1]-x[0]+1
        for q in sorted(qs):
            while i<n and ivals[i][0]<=q:
                heappush(h,(size(ivals[i]),ivals[i][1]))
                i+=1
            
            while h and h[0][1]<q: heappop(h)

            if h: res[q]=h[0][0]
        
        return [res[q] for q in qs]



        