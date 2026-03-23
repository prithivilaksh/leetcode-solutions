# class Solution:
#     def nearestPalindromic(self, n: str) -> str:
#         if int(n) <= 10 or (int(n[0]) == 1 and int(n[1:]) == 0):  # <= 10 or equal to 100, 1000, 10000, ... 
#             return str(int(n) - 1)
#         elif int(n) == 11 or (int(n) % 10 == 1 and n[0] == "1" and int(n[1:-1]) == 0):  # 11 or 101, 1001, 10001, 100001, ... 
#             return str(int(n) - 2)
#         elif n[0] == "9" and n[0] * len(n) == n:  # 99, 999, 9999, 99999, ... 
#             return str(int(n) + 2)
#         else:
#             def build_palindrome(base: str, is_even = True) -> str:
#                 if is_even:
#                     return base + ''.join(reversed(base))
#                 else:
#                     return base[:-1] + base[-1] + ''.join(reversed(base[:-1]))
                
#             is_even = len(n) % 2 == 0
#             base = int(n[0: len(n) // 2]) if is_even else int(n[0: len(n) // 2 + 1])

#             is_pal = build_palindrome(str(base), is_even) == n
#             bases = [base - 1, base + 1] if is_pal else [base - 1, base, base + 1]

#             min_diff = float("inf")
#             for base in bases:
#                 candidate = int(build_palindrome(str(base), is_even))
#                 if abs(candidate - int(n)) < min_diff:
#                     min_diff = abs(candidate - int(n))
#                     min_base_candidate = str(base)
            
#             return build_palindrome(min_base_candidate, is_even)


class Solution:
    def nearestPalindromic(self, n: str) -> str:

        def construct(half):
            half=str(half)
            if ln&1: return half+half[::-1][1:]
            return half+half[::-1]
        
        ln=len(n)
        half,intn=int(n[:ceil(ln/2)]),int(n)

        cand=[construct(half),construct(half-1),construct(half+1),str(10**(ln-1)-1),str(10**ln+1)]
        mindiff,res=inf,None
        for c in cand:
            if c==n: continue
            c=int(c)
            if abs(c-intn)<mindiff:
                mindiff=abs(c-intn)
                res=c
            elif abs(c-intn)==mindiff:
                res=min(res,c)
        return str(res)

        
        


# class Solution:
#     def convert(self, num: int) -> int:
#         s = str(num)
#         n = len(s)
#         l, r = (n - 1) // 2, n // 2
#         s_list = list(s)
#         while l >= 0:
#             s_list[r] = s_list[l]
#             r += 1
#             l -= 1
#         return int("".join(s_list))

#     def previous_palindrome(self, num: int) -> int:
#         left, right = 0, num
#         ans = float("-inf")
#         while left <= right:
#             mid = (right - left) // 2 + left
#             palin = self.convert(mid)
#             if palin < num:
#                 ans = palin
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return ans

#     def next_palindrome(self, num: int) -> int:
#         left, right = num, int(1e18)
#         ans = float("-inf")
#         while left <= right:
#             mid = (right - left) // 2 + left
#             palin = self.convert(mid)
#             if palin > num:
#                 ans = palin
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return ans

#     def nearestPalindromic(self, n: str) -> str:
#         num = int(n)
#         a = self.previous_palindrome(num)
#         b = self.next_palindrome(num)
#         if abs(a - num) <= abs(b - num): return str(a)
#         return str(b)

