# class Solution:
#     def openLock(self, deadends: List[str], target: str) -> int:
        
#         dq=deque(["0000"])
#         vis,d=set(deadends),0
#         if "0000" in vis: return -1

#         while dq:
#             for _ in range(len(dq)):
#                 curr=dq.popleft()
#                 if curr==target: return d
#                 for i in range(4):
#                     x=int(curr[i])
#                     for x in (x+1,x-1):
#                         x%=10
#                         cand=curr[:i]+str(x)+curr[i+1:]
#                         if cand in vis: continue
#                         vis.add(cand)
#                         dq.append(cand)
#             d+=1

#         return -1


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        vis=set(deadends)
        if "0000" in vis or target in vis: return -1
        if "0000"==target: return 0

        dq,d=deque(["0000"]),0
        while dq:
            for _ in range(len(dq)):
                curr=dq.popleft()
                for i in range(4):
                    x=int(curr[i])
                    for x in (x+1,x-1):
                        x%=10
                        cand=curr[:i]+str(x)+curr[i+1:]
                        if cand in vis: continue
                        if cand==target: return d+1
                        vis.add(cand)
                        dq.append(cand)
            d+=1

        return -1