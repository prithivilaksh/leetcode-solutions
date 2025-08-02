# class Solution:
#     def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

#         land,water=[],[]
#         for x,y in zip(landStartTime,landDuration):
#             land.append([x,y])
#         for x,y in zip(waterStartTime,waterDuration):
#             water.append([x,y])

#         land.sort(key=lambda x: x[0]+x[1])
#         water.sort(key=lambda x: x[0]+x[1])

#         res=inf
#         landend=land[0][0]+land[0][1]
#         for x,y in water:
#             res=min(res,max(landend+y,x+y))

#         waterend=water[0][0]+water[0][1]
#         for x,y in land:
#             res=min(res,max(waterend+y,x+y))

#         return res


# class Solution:
#     def earliestFinishTime(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:

#         land,water=[],[]
#         for x,y in zip(ls,ld):land.append([x,y])
#         for x,y in zip(ws,wd):water.append([x,y])

#         land.sort(key=lambda x: x[0]+x[1])
#         water.sort(key=lambda x: x[0]+x[1])

#         res=inf
#         landf=land[0][0]+land[0][1]
#         for x,y in water:
#             if res<x:break
#             res=min(res,max(landf+y,x+y))

#         waterf=water[0][0]+water[0][1]
#         for x,y in land:
#             if res<x:break
#             res=min(res,max(waterf+y,x+y))

#         return res

# class Solution:
#     def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

#         land,water=[],[]
#         for x,y in zip(landStartTime,landDuration):
#             land.append([x,y])
#         for x,y in zip(waterStartTime,waterDuration):
#             water.append([x,y])

#         land.sort(key=lambda x: x[0]+x[1])
#         water.sort(key=lambda x: x[0]+x[1])

#         res=inf
#         landend=land[0][0]+land[0][1]
#         for x,y in water:
#             res=min(res,max(landend+y,x+y))

#         waterend=water[0][0]+water[0][1]
#         for x,y in land:
#             res=min(res,max(waterend+y,x+y))

#         return res


class Solution:
    def earliestFinishTime(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:

        
        landf=min(x+y for x,y in zip(ls,ld))
        watef=min(x+y for x,y in zip(ws,wd))
        
        res=inf
        for x,y in zip(ls,ld):
            res=min(res,max(watef,x)+y)
        for x,y in zip(ws,wd):
            res=min(res,max(landf,x)+y)
        return res
