# class Solution:
#     def generateSchedule(self, n: int) -> List[List[int]]:

#         mat=set()
#         for i in range(n):
#             for j in range(n):
#                 if i!=j: mat.add((i,j))

#         res,tot=[],len(mat)
#         def helper():
#             if len(res)==tot: return
#             for m in mat:
#                 if len(res)!=tot:
#                     if not res or (m[0] not in res[-1] and m[1] not in res[-1]): 
#                         mat.remove(m)
#                         res.append(m)
#                         helper()
#                         if len(res)==tot: return
#                         res.pop()
#                         mat.add(m)
#         helper()
#         return [] if len(res)!=tot else res
        

# class Solution:
#     def generateSchedule(self, n: int) -> List[List[int]]:

#         mat=set()
#         for i in range(n):
#             for j in range(i+1,n):
#                 mat.add((i,j))
#                 mat.add((j,i))

#         res,tot=[],len(mat)
#         def helper():
#             if len(res)==tot: return
#             for m in mat:
#                 if not res or (m[0] not in res[-1] and m[1] not in res[-1]): 
#                     mat.remove(m)
#                     res.append(m)
#                     helper()
#                     if len(res)==tot: return
#                     res.pop()
#                     mat.add(m)
#         helper()
#         return [] if len(res)!=tot else res
        
# class Solution:
#     def generateSchedule(self, n: int) -> List[List[int]]:

#         mat=set()
#         for i in range(n):
#             for j in range(i+1,n):
#                 mat.add((i,j));mat.add((j,i))

#         res=[[-1,-1]]
#         def helper():
#             if not mat: return True
#             for m in mat:
#                 if m[0] not in res[-1] and m[1] not in res[-1]: 
#                     mat.remove(m);res.append(m)
#                     if helper(): return True
#                     res.pop();mat.add(m)

#         return res[1:] if helper() else []

class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:

        mat=set()
        for i in range(n):
            for j in range(i+1,n):
                mat.add((i,j));mat.add((j,i))

        res=[[-1,-1]]
        def helper():
            for m in mat:
                if set(m)&set(res[-1]): continue
                mat.remove(m);res.append(m)
                if not mat or helper(): return True
                res.pop();mat.add(m)

        return res[1:] if helper() else []

# class Solution:
#     def generateSchedule(self, n: int) -> List[List[int]]:

#         mat=set()
#         for i in range(n):
#             for j in range(i+1,n):
#                 mat.add((i,j));mat.add((j,i))

#         res=[[-1,-1]]
#         def helper():
#             for m in mat:
#                 if res[-1][0]==m[0] or res[-1][0]==m[1] or res[-1][1]==m[0] or res[-1][1]==m[1]: continue
#                 mat.remove(m);res.append(m)
#                 if not mat or helper(): return True
#                 res.pop();mat.add(m)

#         return res[1:] if helper() else []
        