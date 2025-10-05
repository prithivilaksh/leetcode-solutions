#TLE
# class Solution:
#     def minimumOneBitOperations(self, n: int) -> int:
        
#         # idea/observation:
#         #     1) negate 0th bit
#         #     2) negate the underlined bit _100..
#         #         a) if the number is of the form 1100.. change it to 0100..
#         #         b) if the number is of the form 0100.. change it to 1100..

#         vis=set([n])
#         dq=deque([n])
#         res=0
#         while dq:
#             for _ in range(len(dq)):
#                 i=dq.popleft()
#                 if i==0: return res
#                 a = i^1 
#                 ith = i & -i
#                 im1th = ith << 1
#                 b = i ^ im1th
#                 if a not in vis: vis.add(a);dq.append(a)
#                 if b not in vis: vis.add(b);dq.append(b)
#             res+=1

#         return -1

#TLE
# class Solution:
#     def minimumOneBitOperations(self, n: int) -> int:
        
#         # idea/observation:
#         #     1) negate 0th bit
#         #     2) negate the underlined bit _100..
#         #         a) if the number is of the form 1100.. change it to 0100..
#         #         b) if the number is of the form 0100.. change it to 1100..

#         vis=set([n])
#         dq=deque([(n,"x")])
#         res=0
#         while dq:
#             for _ in range(len(dq)):
#                 i,op=dq.popleft()
#                 if i==0: return res
#                 a = i^1 
#                 b = i ^ ((i & -i) << 1)
#                 if a not in vis and op!="a": vis.add(a);dq.append((a,"a"))
#                 if b<3*i and b not in vis and op!="b": vis.add(b);dq.append((b,"b"))
#             res+=1

#         return -1


#TLE
# class Solution:
#     def minimumOneBitOperations(self, n: int) -> int:
        
#         # idea/observation:
#         #     1) negate 0th bit
#         #     2) negate the underlined bit _100..
#         #         a) if the number is of the form 1100.. change it to 0100..
#         #         b) if the number is of the form 0100.. change it to 1100..

#         vis=set([n])
#         dq=deque([n])
#         res=0
#         while dq:
#             for _ in range(len(dq)):
#                 i=dq.popleft()
#                 if i==0: return res
#                 a = i^1 
#                 b = i ^ ((i & -i) << 1)
#                 if a not in vis: vis.add(a);dq.append(a)
#                 if b<3*i and b not in vis: vis.add(b);dq.append(b)
#             res+=1

#         return -1

#https://www.youtube.com/watch?v=yRI18_MaG7k
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        
        k = 0
        curr = 1
        while (curr * 2) <= n:
            curr *= 2
            k += 1

        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(n ^ curr)