class Solution:
    def scoreBalance(self, s: str) -> bool:

        sum,st=0,set()
        for c in s:
            sum+=ord(c)-ord('a')+1
            st.add(sum)
        if sum%2==1: return False
        return sum//2 in st

# class Solution:
#     def scoreBalance(self, s: str) -> bool:
#         total = sum(ord(c) - ord('a') + 1 for c in s)
#         prefix = 0
#         for c in s:
#             prefix += ord(c) - ord('a') + 1
#             if 2 * prefix == total:
#                 return True
#         return False