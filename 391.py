# class Solution:
#     def isRectangleCover(self, recs: List[List[int]]) -> bool:
        
#         corners,area=set(),0
#         x1=y1=inf
#         a1=b1=-inf
#         for x,y,a,b in recs:
#             tl,tr=(x,b),(a,b)
#             bl,br=(x,y),(a,y)
            
#             x1=min(x1,x)
#             y1=min(y1,y)
#             a1=max(a1,a)
#             b1=max(b1,b)

#             area+=(a-x)*(b-y)

#             for point in (tl,tr,bl,br):
#                 if point in corners: corners.remove(point)
#                 else: corners.add(point)
        
#         tl,tr=(x1,b1),(a1,b1)
#         bl,br=(x1,y1),(a1,y1)
#         for point in (tl,tr,bl,br): 
#             if point not in corners: 
#                 return False

#         return len(corners)==4 and area==(a1-x1)*(b1-y1)
        

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        corners,tot = set(),0
        area = lambda: (Y-y) * (X-x)
        
        for x, y, X, Y in rectangles:
            tot += area()
            corners ^= {(x,y), (x,Y), (X,y), (X,Y)}

        if len(corners) != 4: return False
        x, y = min(corners, key=lambda p: sum(p))
        X, Y = max(corners, key=lambda p: sum(p))
        return area() == tot