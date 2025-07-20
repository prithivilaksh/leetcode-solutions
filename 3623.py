# class Solution:
#     def countTrapezoids(self, points: List[List[int]]) -> int:
#         MOD = 10**9 + 7
        
#         y_count = defaultdict(int)
#         for x, y in points:
#             y_count[y] += 1
        
#         segment_counts = []
#         for cnt in y_count.values():
#             if cnt >= 2:
#                 segment_counts.append(comb(cnt, 2))

#         total = sum(segment_counts) % MOD
#         square_sum = sum((x * x) % MOD for x in segment_counts) % MOD

#         numerator = (total * total - square_sum) % MOD
#         result = (numerator * pow(2, MOD - 2, MOD)) % MOD

#         return result


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        mp=defaultdict(int)
        for x,y in points:
            mp[y]+=1
        
        res,tot=0,0
        for cnt in mp.values():
            pairs=comb(cnt,2)
            ires=(tot*pairs)%MOD
            res=(res+ires)%MOD
            tot+=pairs
        return res

