class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        
        m,n=len(a),len(b)
        i=j=0
        res=[]
        while i<m and j<n:
            if a[i][1]<b[j][0]:i+=1
            elif b[j][1]<a[i][0]: j+=1
            else:
                res.append([max(a[i][0],b[j][0]),min(a[i][1],b[j][1])])
                if a[i][1]<=b[j][1]: i+=1
                else: j+=1

        return res
        