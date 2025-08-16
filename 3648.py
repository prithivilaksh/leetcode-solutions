class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        k=2*k+1
        a=ceil(m/k)
        b=ceil(n/k)
        return a*b