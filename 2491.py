# class Solution:
#     def dividePlayers(self, skill: List[int]) -> int:
#         skill.sort() 
#         l, r = 0, len(skill) - 1
#         tot = skill[0] + skill[-1]
#         res = 0

#         while l < r:
#             if skill[l]+skill[r]!=tot: return -1
#             res+=skill[l]*skill[r]
#             l += 1
#             r -= 1
#         return res

# class Solution:
#     def dividePlayers(self, skill: List[int]) -> int:
        
#         n,tot=len(skill)//2,sum(skill)
#         if tot%n: return -1
#         skpt,res=tot//n,0

#         s2c=defaultdict(int)
#         for s in skill: s2c[s]+=1

#         for s,c in s2c.items():
#             if c!=s2c[skpt-s]: return -1
#             res+=s*(skpt-s)*c
#         return res//2

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        n,tot=len(skill)//2,sum(skill)
        if tot%n: return -1
        skpt,res=tot//n,0

        s2c=Counter(skill)

        for s,c in s2c.items():
            if c!=s2c[skpt-s]: return -1
            res+=s*(skpt-s)*c
        return res//2