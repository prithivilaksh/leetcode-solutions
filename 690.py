"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# class Solution:
#     def getImportance(self, employees: List['Employee'], id: int) -> int:
        
#         id2em={}
#         for em in employees: id2em[em.id]=em

#         def dfs(id):
#             res=id2em[id].importance
#             for v in id2em[id].subordinates:
#                 res+=dfs(v)
#             return res
        
#         return dfs(id)

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        id2em={}
        for em in employees: id2em[em.id]=em
        
        dq,res=deque([id]),0

        while dq:
            em=id2em[dq.popleft()]
            res+=em.importance
            for v in em.subordinates: dq.append(v)
        
        return res