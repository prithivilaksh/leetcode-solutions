class Solution:
    def visiblePoints(self, points: list[list[int]], angle: int, location: list[int]) -> int:
        
        # idea:
        # 1) sort all points by angle wrt to location
        # 2) line sweep and count using dq

        x,y=location
        arr,extra=[],0

        for i,j in points:
            if i==x and j==y: extra+=1;continue
            arr.append(math.atan2(j-y,i-x))

        arr.sort()
        arr=arr+[a+2*math.pi for a in arr]
        angle=(math.pi*angle)/180

        l,r=0,-1
        for r,x in enumerate(arr):
            if x-arr[l]>angle: l+=1
        return r-l+1+extra

        




