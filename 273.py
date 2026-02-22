class Solution:
    def numberToWords(self, num: int) -> str:
        
        # idea/obs:
        # 1) split into 3s
        # 2) b 987 654 321
        # 3) words are same for parts of 3
        mp={
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",

            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",

            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        def words(x):
            ires=[]
            h=x//100
            t=((x//10)%10)*10
            o=x%10
            to=x%100
            if h: ires+=[mp[h]]+["Hundred"]
            if t==10: ires+=[mp[to]];return ires
            if t: ires+=[mp[t]]
            if o: ires+=[mp[o]]
            return ires

        a=num//1000000000
        b=(num//1000000)%1000
        c=(num//1000)%1000
        d=num%1000

        res=[]
        if a: res+=words(a)+ ["Billion"]
        if b: res+=words(b)+ ["Million"]
        if c: res+=words(c)+ ["Thousand"]
        if d: res+=words(d)

        return " ".join(res) if res else "Zero"