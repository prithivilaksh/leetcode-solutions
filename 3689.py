class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mx,mi=max(nums),min(nums)
        return (mx-mi)*k