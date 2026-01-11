# class Solution:
#     def earliestFullBloom(self, pt: List[int], gt: List[int]) -> int:
        
#         # idea/observation:
#         # 1) if 2 seeds have same plant time but different grow time. pick the one with maximum grow time first
#         # 2) if 2 seeds have different plant time but same grow time. pick anything

#         pg=[(p,g) for p,g in zip(pt,gt)]
#         pg.sort(key=lambda x: (-x[1],x[0]))

#         t=res=0
#         for p,g in pg:
#             t+=p
#             res=max(res,t+g)
#         return res


class Solution:
    def earliestFullBloom(self, pt: List[int], gt: List[int]) -> int:
        
        # idea/observation:
        # 1) if 2 seeds have same plant time but different grow time. pick the one with maximum grow time first
        # 2) if 2 seeds have different plant time but same grow time. pick anything

        pg=[(p,g) for p,g in zip(pt,gt)]
        pg.sort(key=itemgetter(1),reverse=True)

        t=res=0
        for p,g in pg:
            t+=p
            res=max(res,t+g)
        return res
