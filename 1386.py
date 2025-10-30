# #MLE
# class Solution:
#     def maxNumberOfFamilies(self, n: int, rs: List[List[int]]) -> int:
        
#         r2n=defaultdict(set)
#         for r,s in rs: r2n[r].add(s)

#         def check(s,r): return s not in r2n[r]

#         res=0
#         l,m,r=(2,3,4,5),(4,5,6,7),(6,7,8,9)
#         for i in range(1,n+1):
#             left = all(check(s,i) for s in l)
#             right = all(check(s,i) for s in r)
#             if left and right: res+=2
#             elif left or right: res+=1
#             else: res+=all(check(s,i) for s in m)
#         return res


# class Solution:
#     def maxNumberOfFamilies(self, n: int, rs: List[List[int]]) -> int:
        
#         r2n=defaultdict(set)
#         for r,s in rs: r2n[r].add(s)

#         def check(s,r): return s not in r2n[r]

#         res=(n-len(r2n))*2
#         l,m,r=(2,3,4,5),(4,5,6,7),(6,7,8,9)
#         for row in r2n:
#             left = all(check(s,row) for s in l)
#             right = all(check(s,row) for s in r)
#             if left and right: res+=2
#             elif left or right: res+=1
#             else: res+=all(check(s,row) for s in m)
#         return res

class Solution:
    def maxNumberOfFamilies(self, n: int, rs: List[List[int]]) -> int:
        
        row=defaultdict(int)
        for r,s in rs:
            if s==1 or s==10: continue
            row[r]|= 1<<(s-2)

        res=(n-len(row))*2
        for r in row.values():
            cnt=0
            if r & 0b00001111 == 0: cnt+=1
            if r & 0b11110000 == 0: cnt+=1
            if cnt==0 and r & 0b00111100 == 0: cnt+=1
            res+=cnt
        return res