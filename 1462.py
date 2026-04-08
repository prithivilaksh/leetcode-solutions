class Solution:
    def checkIfPrerequisite(self, numCourses: int, prereq: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        pre=defaultdict(set)
        for a,b in prereq:
            pre[b].add(a)
        
        @cache
        def dfs(u):
            res=set()
            for v in pre[u]:
                res|=dfs(v)
            return res|pre[u]
        
        return [u in dfs(v) for u,v in queries]