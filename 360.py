class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # given: 
        #     nums = [x1,x2,x3,...,xn] in sorted order
        #     coefficients a,b,c for ax^2+bx+c
        #     -100 <= nums[i], a, b, c <= 100
        #     1 <= nums.length <= 200

        # apply the transformation to each element of nums and return the sorted array 

        # idea/observation:
        # 1) c will not affect the relative positioning of the elements
        # 2) nums=x=[-1000,-10,-1,0,1,10,1000]
        # 3) x^2=[1000000,100,1,0,1,100,1000000]

        # 4) a>>b a=1000 b=10 ax^2=[1000000000,100000,1000,0,1000,100000,1000000000], bx=[-10000,-100,-10,0,10,100,10000]
        # 5) a>>b a=1000 b=-10 ax^2=[1000000000,100000,1000,0,1000,100000,1000000000], bx=[10000,100,10,0,-10,-100,-10000]
        # 6) a>>b a=-10 b=-1000 ax^2=[-10000000,-1000,-10,0,-10,-1000,-10000000], bx=[1000000,10000,1000,0,-1000,-10000,-1000000]

        # 7) a<<b a=10 b=1000 ax^2=[10000000,1000,10,0,10,1000,10000000], bx=[-1000000,-10000,-1000,0,1000,10000,1000000]
        # 8) a<<b a=-10 b=1000 ax^2=[-10000000,-1000,-10,0,-10,-1000,-10000000], bx=[-1000000,-10000,-1000,0,1000,10000,1000000]
        # 9) a<<b a=-1000 b=-10 ax^2=[-1000000000,-100000,-1000,0,-1000,-100000,-1000000000] bx=[10000,100,10,0,-10,-100,-10000]

        # 10) if a>0, its u curve, the ends will have max values
        # 11) if a<0, its n curve, the ends will have min values

        n=len(nums)
        res=[0]*n
        l,r=0,n-1
        f= lambda x: a*x*x+b*x+c
        ind=n-1 if a>0 else 0

        while l<=r:
            fl,fr=f(nums[l]),f(nums[r])
            if a>0:
                if fl>fr: res[ind]=fl;l+=1
                else: res[ind]=fr;r-=1
                ind-=1
            else:
                if fl<fr: res[ind]=fl;l+=1
                else: res[ind]=fr;r-=1
                ind+=1
        return res 

            

        
        
