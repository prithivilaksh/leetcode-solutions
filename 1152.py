# class Solution:
#     def mostVisitedPattern(
#         self, username: List[str], timestamp: List[int], website: List[str]
#     ) -> List[str]:
#         d = defaultdict(list)
#         for user, _, site in sorted(
#             zip(username, timestamp, website), key=lambda x: x[1]
#         ):
#             d[user].append(site)

#         cnt = Counter()
#         for sites in d.values():
#             m = len(sites)
#             s = set()
#             if m > 2:
#                 for i in range(m - 2):
#                     for j in range(i + 1, m - 1):
#                         for k in range(j + 1, m):
#                             s.add((sites[i], sites[j], sites[k]))
#             for t in s:
#                 cnt[t] += 1
#         return sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[0][0]

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        arr = list(zip(timestamp, username, website))
        arr.sort()

        mp = defaultdict(list)
        for time, user, site in arr:
            mp[user].append(site)

        count = defaultdict(int)
        for user in mp:
            patterns = set()
            cur = mp[user]
            for i in range(len(cur)):
                for j in range(i + 1, len(cur)):
                    for k in range(j + 1, len(cur)):
                        patterns.add((cur[i], cur[j], cur[k]))
            for p in patterns:
                count[p] += 1

        max_count = 0
        res = tuple()
        for pattern in count:
            if count[pattern] > max_count or (count[pattern] == max_count and pattern < res):
                max_count = count[pattern]
                res = pattern

        return list(res)
