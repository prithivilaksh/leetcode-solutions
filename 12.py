
# class Solution:
#     def intToRoman(self, n: int) -> str:

#         map={
#             0: '',
#             1: 'I',
#             2: 'II',
#             3: 'III',
#             4: 'IV',
#             5: 'V',
#             6: 'VI',
#             7: 'VII',
#             8: 'VIII',
#             9: 'IX',
#             10: 'X',
#             20: 'XX',
#             30: 'XXX',
#             40: 'XL',
#             50: 'L',
#             60: 'LX',
#             70: 'LXX',
#             80: 'LXXX',
#             90: 'XC',
#             100: 'C',
#             200: 'CC',
#             300: 'CCC',
#             400: 'CD',
#             500: 'D',
#             600: 'DC',
#             700: 'DCC',
#             800: 'DCCC',
#             900: 'CM',
#             1000: 'M',
#             2000: 'MM',
#             3000: 'MMM'
#         }
    
#         res,tenpow="",1
#         while n:
#             r=n%10
#             n=n//10
#             res=map[r*tenpow]+res
#             tenpow*=10
#         return res


class Solution:
    def intToRoman(self, n: int) -> str:
        map=(
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        )
        res=""
        for i,r in map:
            while i<=n:
                res+=r
                n-=i
        return res 
        