class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        boxes=tuple((color,len(tuple(group))) for color,group in groupby(boxes))

        @cache
        def dp(boxes):
            if not boxes: return 0
            lcolor,lcnt=boxes[0]

            res=lcnt**2+dp(boxes[1:])
            for r,(rcolor,rcnt) in enumerate(boxes[1:],start=1):
                if lcolor==rcolor:
                    res=max(res,dp(boxes[1:r])+dp(((lcolor,lcnt+rcnt),)+boxes[r+1:]))

            return res
        return dp(boxes)

















