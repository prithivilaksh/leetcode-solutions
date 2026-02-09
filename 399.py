class Solution:
    def calcEquation(self, eqs: List[List[str]], vals: List[float], qs: List[List[str]]) -> List[float]:
        
        par,fact,res={},{},[]

        def find(x):
            if x not in par: par[x],fact[x]=x,1
            if par[x]!=x:
                par[x],f=find(par[x])
                fact[x]*=f
            return par[x],fact[x]
        
        def union(a,b,f):
            a,fa=find(a)
            b,fb=find(b)
            if a==b: return
            par[b]=a
            fact[b]= fa * f / fb
        
        for (a,b),v in zip(eqs,vals):
            union(a,b,v)
        
        def divide(a,b):
            if a not in par or b not in par: return -1
            a,fa=find(a)
            b,fb=find(b)
            if a!=b: return -1
            return fb/fa
        
        for a,b in qs:
            res.append(divide(a,b))
        
        return res
