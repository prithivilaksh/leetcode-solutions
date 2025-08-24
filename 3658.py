# class Solution:
#     def gcdOfOddEvenSums(self, n: int) -> int:

#         # observation:
#         #     -2 4 6 8 10 -> 2+10=4+8=6+6
#         #     - tot sum = n/2 * pair sum
#         #     - pair -> a , a+(n-1)d 

#         #     - GCD
#         #     - if d is a common divisor of a,b where a>=b
#         #     - a = q1 d
#         #     - b = q2 d
#         #     - a=b*q + r
#         #     - q1 * d = q2 * d * q +r
#         #     - d (q1-q2q) = r
#         #     - d (whole number) = r
#         #     - d is also a divisor of r (a%b)
#         #     - base case when b==0, a is the greatest common divisor

#         def seriesSum(n,a,d):
#             return (n/2)*(2*a+(n-1)*d)

#         o=int(seriesSum(n,1,2))
#         e=int(seriesSum(n,2,2))

#         def gcd(a,b):
#             if b==0: return a
#             return gcd(b,a%b)

#         return gcd(o,e)

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        # observation:
        #     2 4 6 8 10 = 30
        #     1 3 5 7 9 = 25 
        #     series sum= n/2 * (a + a+(n-1)d)
        #     given d=2, a1=1, a2=a1+1, l1=a1+(n-1)d, l2=l1+1

        #     s1=n/2 (a1+l1) // a1 and l1 are both odd so a1+l1 is divisible by 2
        #     s2=n/2 (a1+l1+2)

        #     n is common

        return n

