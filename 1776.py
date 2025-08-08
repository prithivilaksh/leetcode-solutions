# class Solution:
#     def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:

#         # idea:
#         #     when n=2
#         #     when the two car collides -> same position
#         #     p1+t*s1=p2+t*s2
#         #     p1-p2=t(s2-s1)
#         #     t=(p1-p2)/(s2-s1)
#         #     given that p1<p2 so for a valid time s1>s2

#         #     when n>2
#         #     car1 can meet car2 before/after car2 meets car3
#         #     if car1 meets car2 first then meets car3 res[1]=t12
#         #     if car2 meets car3 first then car1 meets res[1]=t13
#         n=len(cars)
#         res,st=[inf]*n,[]
#         for i in range(n-1,-1,-1):
#             p1,s1=cars[i]
#             while st:
#                 p2,s2=cars[st[-1]]
#                 t=(p1-p2)/(s2-s1) if s2!=s1 else inf
#                 if s1<=s2: st.pop()
#                 elif t>=res[st[-1]]: st.pop()
#                 else: 
#                     res[i]=t
#                     break
#             st.append(i)
#         return [-1 if x==inf else x for x in res]


# class Solution:
#     def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:

#         # idea:
#         #     when n=2
#         #     when the two car collides -> same position
#         #     p1+t*s1=p2+t*s2
#         #     p1-p2=t(s2-s1)
#         #     t=(p1-p2)/(s2-s1)
#         #     given that p1<p2 so for a valid time s1>s2

#         #     when n>2
#         #     car1 can meet car2 before/after car2 meets car3
#         #     if car1 meets car2 first then meets car3 res[1]=t12
#         #     if car2 meets car3 first then car1 meets res[1]=t13
#         n=len(cars)
#         res,st=[-1]*n,[]
#         for i in range(n-1,-1,-1):
#             p1,s1=cars[i]
#             while st:
#                 p2,s2=cars[st[-1]]
#                 if s1<=s2: st.pop()
#                 else:
#                     t=(p1-p2)/(s2-s1) 
#                     if t>=res[st[-1]] and res[st[-1]]!=-1: st.pop()
#                     else: res[i]=t;break
#             st.append(i)
#         return res


# class Solution:
#     def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:

#         # idea:
#         #     when n=2
#         #     when the two car collides -> same position
#         #     p1+t*s1=p2+t*s2
#         #     p1-p2=t(s2-s1)
#         #     t=(p1-p2)/(s2-s1)
#         #     given that p1<p2 so for a valid time s1>s2

#         #     when n>2
#         #     car1 can meet car2 before/after car2 meets car3
#         #     if car1 meets car2 first then meets car3 res[1]=t12
#         #     if car2 meets car3 first then car1 meets res[1]=t13
        
#         h=[]
#         n=len(cars)
#         for i in range(n-1):
#             (p1,s1),(p2,s2)=cars[i],cars[i+1]
#             if s1>s2:
#                 t=((p1-p2)/(s2-s1)) 
#                 heappush(h,(t,i))
        

#         next=[i+1 for i in range(n)]
#         prev=[i-1 for i in range(n)]
#         res=[-1]*n
#         while h:
#             t,i=heappop(h)
#             if res[i]!=-1: continue
#             res[i]=t
#             next[prev[i]]=next[i]
#             prev[next[i]]=prev[i]
#             if prev[i]<0 or res[prev[i]]!=-1: continue
#             (p1,s1),(p2,s2)=cars[prev[i]],cars[next[i]]
#             if s1>s2:
#                 t=((p1-p2)/(s2-s1)) 
#                 heappush(h,(t,prev[i]))
#         return res


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:

        # idea:
        #     when n=2
        #     when the two car collides -> same position
        #     p1+t*s1=p2+t*s2
        #     p1-p2=t(s2-s1)
        #     t=(p1-p2)/(s2-s1)
        #     given that p1<p2 so for a valid time s1>s2

        #     when n>2
        #     car1 can meet car2 before/after car2 meets car3
        #     if car1 meets car2 first then meets car3 res[1]=t12
        #     if car2 meets car3 first then car1 meets res[1]=t13
        n=len(cars)
        res,st=[inf]*n,[]
        for i in range(n-1,-1,-1):
            p1,s1=cars[i]
            while st:
                p2,s2=cars[st[-1]]
                if s1<=s2: st.pop()
                else:
                    t=(p1-p2)/(s2-s1) 
                    if t>=res[st[-1]]: st.pop()
                    else: res[i]=t;break
            st.append(i)
        return [-1 if x==inf else x for x in res]