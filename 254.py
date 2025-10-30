class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        res,path=[],[]
        def dfs(n,s):
            if path: res.append(path+[n])
            i=s
            while i*i<=n:
                if n%i==0:
                    path.append(i)
                    dfs(n//i,i)
                    path.pop()
                i+=1
        dfs(n,2)
        return res