class Solution:
    def checkRecord(self, n: int) -> int:
        

        # idea
        # - total permutations 3^n
        # - there can be 0 or 1 As
        # - there can be L, LL

        # - track
        #     - ways with 1 A
        #         - ways beginning with 0 L
        #         - ways beginning with 1 L
        #         - ways beginning with 2 L
        #     - ways with 0 A
        #         - ways beginning with 0 L
        #         - ways beginning with 1 L
        #         - ways beginning with 2 L
        #     - tot valid
        M=10**9+7
        def dp(n):
            if n==1: return 1,0,0,1,1,0
            n1a0l,n1a1l,n1a2l,n0a0l,n0a1l,n0a2l=dp(n-1)

            c1a0l=(n1a0l + n1a1l + n1a2l + n0a0l + n0a1l + n0a2l)%M
            c1a1l=n1a0l
            c1a2l=n1a1l

            c0a0l=(n0a0l + n0a1l + n0a2l)%M
            c0a1l=n0a0l
            c0a2l=n0a1l

            return c1a0l,c1a1l,c1a2l,c0a0l,c0a1l,c0a2l

        return sum(dp(n)) % M
