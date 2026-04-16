class Solution(object):
    def longestConsecutive(self, root):

        def dfs(node):
            if not node: return None,0,0
            x,inc1,dec1=dfs(node.left)
            y,inc2,dec2=dfs(node.right)

            inc=dec=1
            if x:
                if node.val+1==x: inc=max(inc,1+inc1)
                if node.val-1==x: dec=max(dec,1+dec1)
            if y:
                if node.val+1==y: inc=max(inc,1+inc2)
                if node.val-1==y: dec=max(dec,1+dec2)
            
            # if x and y:
            #     if x+1==node.val==y-1: res[0]=max(res[0],dec1+1+inc2)
            #     if x-1==node.val==y+1: res[0]=max(res[0],inc1+1+dec2)
            
            res[0]=max(res[0],inc,dec,inc+dec-1)
            return node.val,inc,dec
        res=[0]
        dfs(root)
        return res[0]
            