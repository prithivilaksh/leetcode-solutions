# class Solution:
#     def maxTotal(self, value: List[int], limit: List[int]) -> int:

#         mp=defaultdict(list)
#         for v,l in sorted(zip(value,limit),reverse=True):
#             mp[l].append(v)

#         res=0
#         for l in sorted(mp):
#             cnt=0
#             for x in mp[l]:
#                 if cnt==l: break
#                 res+=x
#                 cnt+=1

#         return res

# class Solution:
#     def maxTotal(self, value: List[int], limit: List[int]) -> int:

#         mp=defaultdict(list)
#         for v,l in sorted(zip(value,limit),reverse=True):
#             mp[l].append(v)

#         res=0
#         for l in mp:
#             cnt=0
#             for x in mp[l]:
#                 if cnt==l: break
#                 res+=x;cnt+=1

#         return res


class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:

        mp=defaultdict(list)
        for v,l in sorted(zip(value,limit),reverse=True):
            mp[l].append(v)

        res=0
        for l in mp:
            res+=sum(mp[l][:l])

        return res