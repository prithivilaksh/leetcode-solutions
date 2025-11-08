from typing import List, Dict

class SparseVector:
    def __init__(self, nums: List[int]) -> None:
        self.non_zero_ele= { i:x for i,x in enumerate(nums) if x!=0}


    def dotProduct(self, vec: "SparseVector") -> int:
        a = self.non_zero_ele
        b = vec.non_zero_ele
        if len(b) < len(a): a, b = b, a
        return sum(ax * b.get(i, 0) for i, ax in a.items())


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)