# class Solution:
#     def canMeasureWater(self, x: int, y: int, t: int) -> bool:
        
#         vis=set()
#         def backtrack(a,b):
#             if (a,b) in vis: return False
#             vis.add((a,b))
#             if a+b==t: return True

#             if a>0 and y-b>0:
#                 if a<y-b: na,nb=0,b+a
#                 else: na,nb=a-(y-b),y
#                 if backtrack(na,nb): return True
            
#             if b>0 and x-a>0:
#                 if b<x-a: na,nb=a+b,0
#                 else: na,nb=x,b-(x-a)
#                 if backtrack(na,nb): return True
            
#             if x!=a and backtrack(x,b): return True
#             if y!=b and backtrack(a,y): return True

#             if a!=0 and backtrack(0,b): return True
#             if b!=0 and backtrack(a,0): return True

#             return False
        
#         return backtrack(0,0)


# class Solution:
#     def canMeasureWater(self, x: int, y: int, t: int) -> bool:
        
#         vis=set()
#         def dfs(tot):
#             if tot==t: return True
#             if tot in vis: return False
#             vis.add(tot)
#             for step in (x,y,-x,-y):
#                 if 0<=tot+step<=x+y and dfs(tot+step): return True
#             return False
        
#         return dfs(0)
            
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        q = deque([0])
        steps = [x, y, -x, -y]
        if x + y < target:
            return False
        seen = set()    
        while q:
            curr = q.popleft()
            for step in steps:
                total = curr + step

                if total == target:
                    return True
                elif total not in seen and 0 <= total <= x + y:
                    seen.add(total)
                    q.append(total)
        return False