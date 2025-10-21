# class Solution:
#     def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
#         avl,unavl,res=[(w,i) for i,w in enumerate(servers)],[],[]
#         heapify(avl)

#         for st,dur in enumerate(tasks):
#             while unavl and unavl[0][0]<=st:
#                 et,w,i=heappop(unavl)
#                 heappush(avl,(w,i))
#             if not avl:
#                 et,w,i=heappop(unavl)
#                 st=max(st,et)
#                 heappush(avl,(w,i))

#             w,i=heappop(avl)
#             heappush(unavl,(st+dur,w,i))
#             res.append(i)
        
#         return res


# class Solution:
#     def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
#         avl,unavl,res=[(w,i) for i,w in enumerate(servers)],[],[]
#         heapify(avl)

#         for st,dur in enumerate(tasks):
#             while unavl and unavl[0][0]<=st:
#                 et,w,i=heappop(unavl)
#                 heappush(avl,(w,i))
#             if not avl:
#                 et,w,i=heappop(unavl)
#                 st=max(st,et)
#             else: w,i=heappop(avl)
#             heappush(unavl,(st+dur,w,i))
#             res.append(i)
        
#         return res


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        avl,unavl,res=[(w,i) for i,w in enumerate(servers)],[],[]
        heapify(avl)

        for st,dur in enumerate(tasks):
            while unavl and unavl[0][0]<=st:
                et,w,i=heappop(unavl)
                heappush(avl,(w,i))
            if not avl:
                et,w,i=heappop(unavl)
                st=et
            else: w,i=heappop(avl)
            heappush(unavl,(st+dur,w,i))
            res.append(i)
        
        return res
