class Solution:
    def countHighestScoreNodes(self, par: List[int]) -> int:
        
        n=len(par)

        chi=defaultdict(list)
        for c,p in enumerate(par):
            chi[p].append(c)

        @cache     
        def size(x):
            sz=1
            for c in chi[x]: sz+=size(c)
            return sz
        
        res=[0,0]
        for p in range(n):
            prod=1
            for c in chi[p]: prod*=size(c)
            if p!=0: prod*=size(0)-size(p)
            if prod>res[0]: res=[prod,1]
            elif prod==res[0]: res[1]+=1

        return res[1]