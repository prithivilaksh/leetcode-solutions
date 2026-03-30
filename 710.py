# class Solution:

#     def __init__(self, n: int, blacklist: List[int]):
#         self.N=n-len(blacklist)
#         self.mp=mp={x:-1 for x in blacklist}

#         i=n-1
#         for x in blacklist:
#             if x>=self.N: continue
#             while i in mp: i-=1
#             mp[x]=i
#             i-=1
        
#     def pick(self) -> int:
#         r=random.randint(0,self.N-1)
#         return self.mp.get(r,r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()


from random import randint

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        blacklist = set(blacklist) 
        self.m = n - len(blacklist)
        key = [x for x in blacklist if x < self.m]
        val = [x for x in range(self.m,n) if x not in blacklist]
        self.mp = dict(zip(key, val))

    def pick(self) -> int:
        i = randint(0, self.m-1)
        return self.mp.get(i, i)