class Solution:
    def uniqueLetterString(self, s: str) -> int:

        c2i,n,res=defaultdict(list),len(s),0
        
        for i,c in enumerate(s): c2i[c].append(i)
        
        for v in c2i.values():
            v=[-1]+v+[n]
            for i in range(1,len(v)-1):
                left=v[i]-v[i-1]
                right=v[i+1]-v[i]
                res+=left*right
        
        return res
        

            