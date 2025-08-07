# class Solution:
#     def carFleet(self, t: int, pos: List[int], speed: List[int]) -> int:
        
#         n=len(pos)
#         time=[0]*n

#         for i,p in enumerate(pos):
#             dis=t-p
#             time[i]=dis/float(speed[i])
        
#         posTime= [(p,t) for p,t in zip(pos,time)]
#         posTime.sort()

#         res=n

#         st=[]
#         for i,(p,t) in enumerate(posTime):
#             while st and st[-1]<=t: st.pop()
#             st.append(t)
#         return len(st)

# class Solution:
#     def carFleet(self, t: int, pos: List[int], speed: List[int]) -> int:
        

#         for i,p in enumerate(pos):
#             dis=t-p
#             time=dis/speed[i]
#             pos[i]=[p,time]
#         posTime=pos
#         posTime.sort()

#         n=res=len(posTime)
#         for i in range(n-1,0,-1):
#             if posTime[i-1][1]<=posTime[i][1]:
#                 res-=1
#                 posTime[i-1]=posTime[i]
#         return res


# class Solution:
#     def carFleet(self, t: int, pos: List[int], speed: List[int]) -> int:
        
#         res,nextTime=len(pos),0
#         for p,s in sorted(zip(pos,speed))[::-1]:
#             dis=t-p
#             time=dis/s
#             if time<=nextTime: res-=1
#             else: nextTime=time
            
#         return res

# class Solution:
#     def carFleet(self, t: int, pos: List[int], speed: List[int]) -> int:
        
#         res=nextTime=0
#         for p,s in sorted(zip(pos,speed))[::-1]:
#             time=(t-p)/s
#             if time>nextTime: 
#                 res+=1
#                 nextTime=time
            
#         return res

class Solution:
    def carFleet(self, t: int, pos: List[int], speed: List[int]) -> int:
        
        st=[]
        for p,s in sorted(zip(pos,speed)):
            time=(t-p)/s
            while st and st[-1]<=time:st.pop()
            st.append(time)
            
        return len(st)

        
