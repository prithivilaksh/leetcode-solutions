# from sortedcontainers import SortedSet
# class TaskManager:

#     def __init__(self, tasks: List[List[int]]):
#         self.p=SortedSet()
#         self.t2u={}
#         self.p2t=defaultdict(lambda : SortedSet())
#         self.t2p={}

#         for uid,tid,pty in tasks: self.add(uid,tid,pty)
        
#     def _getstate(self): return self.p,self.t2u,self.p2t,self.t2p

#     def add(self, uid: int, tid: int, pty: int) -> None:
#         p,t2u,p2t,t2p=self._getstate()
#         p.add(pty)
#         t2u[tid]=uid
#         p2t[pty].add(tid)
#         t2p[tid]=pty
        

#     def edit(self, tid: int, newpty: int) -> None:
#         p,t2u,p2t,t2p=self._getstate()

#         oldpty=t2p[tid]
#         p2t[oldpty].discard(tid)
#         if len(p2t[oldpty])==0: 
#             del p2t[oldpty]
#             p.discard(oldpty)
        
#         p.add(newpty)
#         p2t[newpty].add(tid)
#         t2p[tid]=newpty

        

#     def rmv(self, tid: int) -> None:
#         p,t2u,p2t,t2p=self._getstate()

#         oldpty=t2p[tid]
#         p2t[oldpty].discard(tid)
#         if len(p2t[oldpty])==0: 
#             del p2t[oldpty]
#             p.discard(oldpty)
        
#         del t2u[tid]
#         del t2p[tid]



#     def execTop(self) -> int:
#         p,t2u,p2t,t2p=self._getstate()
#         if not p: return -1
#         mxpty=p[-1]
#         tid=p2t[mxpty].pop()
#         uid=t2u[tid]

#         if len(p2t[mxpty])==0: 
#             del p2t[mxpty]
#             p.discard(mxpty)
        
#         del t2u[tid]
#         del t2p[tid]

#         return uid
        


# # Your TaskManager object will be instantiated and called as such:
# # obj = TaskManager(tasks)
# # obj.add(userId,taskId,priority)
# # obj.edit(taskId,newPriority)
# # obj.rmv(taskId)
# # param_4 = obj.execTop()


# from sortedcontainers import SortedSet
# class TaskManager:

#     def __init__(self, tasks: List[List[int]]):
#         self.p=SortedSet()
#         self.t2u={}
#         self.p2t=defaultdict(lambda : SortedSet())
#         self.t2p={}
#         for uid,tid,pty in tasks: self.add(uid,tid,pty)
        
#     def _getstate(self): return self.p,self.t2u,self.p2t,self.t2p

#     def add(self, uid: int, tid: int, pty: int) -> None:
#         p,t2u,p2t,t2p=self._getstate()
#         p.add(pty)
#         t2u[tid]=uid
#         p2t[pty].add(tid)
#         t2p[tid]=pty
        

#     def edit(self, tid: int, newpty: int) -> None:
#         uid,tid,pty = self._rmv(tid)
#         self.add(uid,tid,newpty)
    
#     def _rmv(self,tid=None):
#         p,t2u,p2t,t2p=self._getstate()
#         if tid==None:
#             if not p: return -1,0,0
#             mxpty=p[-1]
#             tid=p2t[mxpty].pop() 

#         pty=t2p[tid]
#         uid=t2u[tid]

#         p2t[pty].discard(tid)
#         if len(p2t[pty])==0: 
#             del p2t[pty]
#             p.discard(pty)
        
#         del t2u[tid]
#         del t2p[tid]       
#         return uid,tid,pty

#     def rmv(self, tid: int) -> None: self._rmv(tid)

#     def execTop(self) -> int: return self._rmv()[0]
        


# # Your TaskManager object will be instantiated and called as such:
# # obj = TaskManager(tasks)
# # obj.add(userId,taskId,priority)
# # obj.edit(taskId,newPriority)
# # obj.rmv(taskId)
# # param_4 = obj.execTop()



class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.h,self.t2u,self.t2p=[],{},{}
        for uid,tid,pty in tasks: self.add(uid,tid,pty) 

    def _getstate(self): return self.h,self.t2u,self.t2p

    def add(self, uid: int, tid: int, pty: int) -> None:
        h,t2u,t2p=self._getstate()
        t2u[tid] = uid
        t2p[tid] = pty
        heappush(h, (-pty,-tid))

    def edit(self, tid: int, pty: int) -> None:
        h,t2u,t2p=self._getstate()
        t2p[tid] = pty
        heappush(h, (-pty,-tid))

    def rmv(self, tid: int) -> None:
        h,t2u,t2p=self._getstate()
        del t2p[tid]
        del t2u[tid]

    def execTop(self) -> int:
        h,t2u,t2p=self._getstate()
        while h:
            pty, tid = heappop(h)
            pty, tid = -pty, -tid
            if t2p.get(tid) == pty:
                del t2p[tid]
                return t2u.pop(tid)
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()