# class Solution:
#     def grayCode(self, n: int) -> List[int]:
        
#         twon=2**n
#         def backtrack(acc,vis):
#             if len(acc)==twon : return (0^acc[-1]).bit_count()==1
#             curr=acc[-1]
#             for i in range(16):
#                 next=curr^(1<<i)
#                 if next in vis: continue
#                 vis.add(next)
#                 acc.append(next)
#                 if backtrack(acc,vis): return True
#                 vis.discard(next)
#                 acc.pop()
#             return False
#         acc,vis=[0],set([0])
#         backtrack(acc,vis)
#         return acc

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for bit in range(n):
            add = 1 << bit

            for x in reversed(ans):
                ans.append(x | add)

        return ans        

        # 0

        # 00 01

        # 00 01 11 10

        # 00 01 11 10 110 111 101 100

        # 0 1 3 2 6 7 5 4
        